from flask import Flask
from flask_restful import reqparse, Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT, jwt_required
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://xdjdzwflubsbjj:0d4c6657d92f66fb060d04a7a2ea3e0a5ba72cec8ccc2dae42eabea0de814b8b@ec2-52-23-40-80.compute-1.amazonaws.com:5432/d6l3uvcb2m9r53" # 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;
app.config['SECRET_KEY'] = 'super-secret'


db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

from models import *


def authenticate(usern, password):
    user = User.query.filter_by(username = usern).first()
    if user and check_password_hash(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    print(user_id)
    return User.query.filter_by(id = user_id).first()


jwt = JWT(app, authenticate, identity)
 
parser = reqparse.RequestParser()

class Homepage(Resource):
    @jwt_required()
    def get(self):
        return {'message':'hola mundo'}    

class UserApi(Resource):
    def get(self,idd):
        return user_schema.dump(User.query.get(1)) #filter_by(id=idd).first()

    def put(self,idd):
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        arg = parser.parse_args()
        user = User.query.filter_by(id = idd).first()
        user.username = arg.username
        db.session.commit()



class UsersApi(Resource):
    def get(self):
        return users_schema.dump(User.query.all())
    def post(self):
        arg =  parser.parse_args()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('email', type=str, required=True)

        return arg

api.add_resource(Homepage, "/")
api.add_resource(UserApi,"/user/<idd>")
api.add_resource(UsersApi, "/users")


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)