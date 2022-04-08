from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):

    def get(self, name, test):
        return {"data": name, "type": test}

    def post(self):
        return {"data": "hello world"}


api.add_resource(HelloWorld, "/whatsapp/<string:name>/<string:test>")

if __name__ == "__main__":
    app.run(debug=True)
