import requests, json
from clarifai import rest
from clarifai.rest import ClarifaiApp
import time
'''
A new way to to get your daily dose of news. Uses the NYT API, Twilio, and Clarifai.
Grabs articles daily from NYT, parse through the data for image links.
Sends image links to Clarifai for image recognition. Get "The most frequent" results (arbitrary term)
sends you a text with twilio with the lines "Today's news consists of "Dogs", "Election, "Whatever".

Bonus: (hard as shit to do, I think)
We make a web app, that displays only the images that we got from NYT. It's like a newspaper without words!!!1!
requires flask
'''

r = requests.get('https://api.nytimes.com/svc/topstories/v2/home.json?api-key=***REMOVED***)
#print(r.json()["response"]["docs"])

data = r.json()

app = ClarifaiApp(***REMOVED***, ***REMOVED***)

for result in data["results"]:
    for media in result["multimedia"]:
        if media["format"] == "superJumbo":
            model = app.models.get("aaa03c23b3724a16a56b629203edc62c")

            result = model.predict_by_url(url=media["url"])
            print(result.get("outputs")[0].get("data").get("concepts")[0])
            print(result.get("outputs")[0].get("data").get("concepts")[1])
            print(result.get("outputs")[0].get("data").get("concepts")[2])
