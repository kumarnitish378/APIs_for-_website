import smtplib, ssl
from flask import Flask
from flask_restful import Api, Resource

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
        return e
    finally:
        server.quit()

message = """From:Jivans software and Engineering <hacktheworld378@gmail.com>
To: To Nitish <nitish.ns377@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: Email Test

This is an e-mail message to be sent in HTML format Nitish

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

class Email(Resource):

    def get(self, to, subject, body):

        body="From:Jivans software and Engineering <hacktheworld378@gmail.com> To: To Nitish <{b}> MIME-Version: 1.0 Content-type: text/html Subject: {c} This is an e-mail message to be sent in HTML format Nitish <b>This is HTML message.</b> <h1>This is headline.</h1> {d}".format(b=to,c=subject,d=body)
        a = EmailOTP(body)
        return {"To":to,"Status":a}

    def post(self):
        return {"data": "hello world"}

api.add_resource(Email, "/email/<string:to>/<string:subject>/<string:body>")

if __name__ == "__main__":
    app.run(debug=True)


# EmailOTP(message)

lst = [1,4,5,5,5,5]
tpl = ()