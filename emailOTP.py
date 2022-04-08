import smtplib, ssl
from flask import Flask
from flask_restful import Api, Resource
from random import randint
import os
from twilio.rest import Client

app = Flask(__name__)
api = Api(app)

def EmailOTP(message):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email ="hacktheworld378@gmail.com" # "jivanspvtltd@gmail.com"
    receivers = "nitish.ns377@gmail.com"
    password = "7004969879nitish" #"tmlvpyrwpzizzwpk"
    # Create a secure SSL context
    context = ssl.create_default_context()
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        # TODO: Send email here
        server.sendmail(sender_email, receivers, message)
        return "Successfully sent email"

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()

checkOTP = 0
def OTPGenerate():
    checkOTP = randint(1000,9999)
    print(checkOTP, file=open("EOPT.txt", 'w'))
    return checkOTP

class OTP(Resource):

    def get(self):

        mobileOTP = OTPGenerate()
        body='Hi there! this is OTP Verification test. your OTP is {} please do not share with any one.'.format(mobileOTP)
        EmailOTP(body)
        return {"Your OTP is":mobileOTP}

    def post(self):
        return {"data": "hello world"}


class verifyOTP(Resource):

    def get(self,otp):

        with open("F:\API\EOPT.txt", "r") as f:
            temp = f.read()
            temp = temp.replace("\n","")
        if temp == otp:
            print(" ", file=open("EOPT.txt", 'w'))
            return {"login": "login Succesful"} #we can change Value
        else:
            return {"login":"login fail", "otp":otp, "Valid OTP":temp}

api.add_resource(OTP, "/user/verifyEmailOTP")
api.add_resource(verifyOTP, "/verifyotp/<string:otp>")

if __name__ == "__main__":
    app.run(debug=True)