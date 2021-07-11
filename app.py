from threading import current_thread
from flask import Flask
from flask_restful import reqparse, Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT, jwt_required, current_identity
from flask_marshmallow import Marshmallow
from flask_cors import CORS,cross_origin
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
cors = CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] =  "postgresql://xdjdzwflubsbjj:0d4c6657d92f66fb060d04a7a2ea3e0a5ba72cec8ccc2dae42eabea0de814b8b@ec2-52-23-40-80.compute-1.amazonaws.com:5432/d6l3uvcb2m9r53" # 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;
app.config['SECRET_KEY'] = 'super-secret'
app.config['CORS_ENABLED'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)

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
    @cross_origin()
    def get(self):
        return {'message':'hola mundo'}    

class MeApi(Resource):
    @cross_origin
    def get(self):
        return current_identity

class UserApi(Resource):
    @cross_origin()
    def get(self,idd):
        return user_schema.dump(User.query.get(1)) #filter_by(id=idd).first()
    @cross_origin()
    def put(self,idd):
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        arg = parser.parse_args()
        user = User.query.filter_by(id = idd).first()
        user.username = arg.username
        db.session.commit()


class UsersApi(Resource):
    @cross_origin()
    def get(self):
        return users_schema.dump(User.query.all())
    @cross_origin()
    def post(self):
        arg =  parser.parse_args()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        return arg

api.add_resource(Homepage, "/")
api.add_resource(UserApi,"/user/<idd>")
api.add_resource(UsersApi, "/users")
api.add_resource(MeApi,"/me")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)