import requests, json
from clarifai import rest
from clarifai.rest import ClarifaiApp
from flask import Flask, render_template, request
import twilio.twiml
from twilio.rest import Client

'''
A new way to to get your daily dose of news. Uses the NYT API, Twilio, and Clarifai.
Grabs articles daily from NYT, parse through the data for image links.
Sends image links to Clarifai for image recognition. Get "The most frequent" results (arbitrary term)
sends you a text with twilio with the lines "Today's news consists of "Dogs", "Election, "Whatever".

Bonus: (hard as shit to do, I think)
We make a web app, that displays only the images that we got from NYT. It's like a newspaper without words!!!1!
requires flask
'''
app = Flask(__name__)

app.config['DEBUG'] = True

client = Client(***REMOVED***, ***REMOVED***)

@app.route('/', methods=['GET', 'POST'])
def hello():
    r = requests.get('https://api.nytimes.com/svc/topstories/v2/home.json?api-key=***REMOVED***)
    data = r.json()
    global wordbank2
    global unalteredwb
    wordbank = []
    urlslist = []

    app = ClarifaiApp(***REMOVED***, ***REMOVED***)
    x = 1
    for result in data["results"]:
        for media in result["multimedia"]:
            if media["format"] == "superJumbo":
                model = app.models.get("aaa03c23b3724a16a56b629203edc62c")
                result = model.predict_by_url(url=media["url"])
                urlslist.append(media["url"])
                print(result.get("outputs")[0].get("data").get("concepts")[0])
                wordbank.append(result.get("outputs")[0].get("data").get("concepts")[0].get("name"))
    unalteredwb = str(wordbank)
    wordbank2 = str(set(wordbank))
    print("The wordbank is " + "".join(str(e) for e in wordbank2))

    return render_template("index.html", image1=urlslist[0], image2=urlslist[1], image3=urlslist[2], image4=urlslist[3], image5=urlslist [4], image6=urlslist[5], image7=urlslist[6], image8=urlslist[7], image9=urlslist[8], image10=urlslist[9],)

@app.route('/sms', methods=['POST'])

def sms():
    number = request.form['From']

    message = client.api.account.messages.create(to=number,
                                                  from_=***REMOVED***,
                                                  body="In today's Top Stories we have: " + wordbank2)
    if "input" in wordbank2:
        location = [i for i,x in enumerate(unalteredwb) if x=="input"]
        for fruit in location
            printoururls = print()
        message = client.api.account.messages.create(to=number,
                                                     from_=***REMOVED***,
                                                     body=printoururls)

    return 'this'
if __name__ == "__main__":
    app.run()

