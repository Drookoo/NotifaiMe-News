from twilio.rest import Client
from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

# Download the Python helper library from twilio.com/docs/python/install
# Your Account Sid and Auth Token from twilio.com/user/account

client = Client(SID, AUTH)


# message = client.messages("PN215931130033d599b663dda10f665ea1") \
#  .fetch()
@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']

    message = client.api.account.messages.create(to=number,
                                                  from_=TWILIO_NUMBER
                                                  body="It works now!!")
    return 'this'


if __name__ == '__main__':
    app.run()
