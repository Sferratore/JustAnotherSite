from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "All my FELLAS!!"

@app.route('/summon')
def summon_meme():
    url = "https://meme.breakingbranches.tech/api?limit=1&type=dank"
    #requests.request("GET", url) sends a GET request to the specified URL.
    #.text extracts the text content from the response.
    #json.loads(...) uses the json module to load (parse) the JSON-formatted text into a Python data structure. The loads function is used for parsing a JSON string.
    response = json.loads(requests.request("GET", url).text)
    meme = response["memes"][0]
    return render_template("index.html", meme_title = meme["title"], meme_url = meme["url"], meme_author = meme["author"])

app.run()  