from flask import Flask
from flask_restful import Api, Resource
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO user (email, userid, password, conformPassword) VALUES ('abc1', 'cde1', 'xyz1', 'xyz1');")



app = Flask(__name__)
api = Api(app)


class SignUp(Resource):

    def get(self, name, test):
        mycursor.execute("INSERT INTO user (email, userid, password, conformPassword) VALUES ({}, {}, 'xyz1', 'xyz1');".format(name, test))

        return {"data": name, "type": test}

    def post(self):
        return {"data": "hello world"}


api.add_resource(SignUp, "/login/<string:name>/<string:test>")

if __name__ == "__main__":
    app.run(debug=True)
