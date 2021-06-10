from flask import Flask
from datetime import datetime
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

class Saludo(Resource):
    def get(self):
        return {'hello':"world"}


api.add_resource(Saludo, "/api")

@app.route('/')
def homepage():
    the_time = 234

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400">
    """.format(time=the_time)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)