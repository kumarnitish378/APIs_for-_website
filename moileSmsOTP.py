from flask import Flask
from flask_restful import Api, Resource
from random import randint
import os
from twilio.rest import Client


app = Flask(__name__)
api = Api(app)

# Twillio Account Setting
account_sid = "ACa329f183f9bbd941d06b524e202df2f9"
auth_token = "4fd9ff750a5a950a0bc296e6a90d2282"
client = Client(account_sid, auth_token)


checkOTP = 0
def OTPGenerate():
    checkOTP = randint(1000,9999)
    print(checkOTP, file=open("otp.txt", 'w'))
    return checkOTP

class OTP(Resource):

    def get(self):

        mobileOTP = OTPGenerate()
        message = client.messages.create(
            body='Hi there! this is OTP Verification test. your OTP is {} please do not share with any one.'.format(mobileOTP) ,
            from_='+12515729753',
            to='+917004969879'
        )
        return {"Your OTP is":mobileOTP}

    def post(self):
        return {"data": "hello world"}


class verifyOTP(Resource):

    def get(self,otp):

        with open("otp.txt", "r") as f:
            temp = f.read()
            temp = temp.replace("\n","")
        if temp == otp:
            print(" ", file=open("otp.txt", 'w'))
            return {"login": "login Succesful"} #we can change Value
        else:
            return {"login":"login fail", "otp":otp, "Valid OTP":temp}

api.add_resource(OTP, "/verifyMobileOTP")
api.add_resource(verifyOTP, "/verifyotp/<string:otp>")

if __name__ == "__main__":
    app.run(debug=True)
