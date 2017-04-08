from flask import Flask, request
from twilio import twiml

app = Flask(__name__)

#promo code = HackNYSpring2017
#ngrok is like heroku?

@app.route('/sms', methods =['POST'])
def sms():
    res = twiml.Response()
    res.message("Thank you!")

