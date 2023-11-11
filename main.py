from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
     return render_template("number.html")

@app.route('/summon', methods=['POST'])
def summon_meme():
    meme_index = int(request.form.get('coolNumber'))
    url = f"https://meme.breakingbranches.tech/api?limit={meme_index}&type=dank"
    #requests.request("GET", url) sends a GET request to the specified URL.
    #.text extracts the text content from the response.
    #json.loads(...) uses the json module to load (parse) the JSON-formatted text into a Python data structure. The loads function is used for parsing a JSON string.
    response = json.loads(requests.request("GET", url).text)
    meme = response["memes"][int(meme_index - 1)]
    return render_template("meme.html", meme_title = meme["title"], meme_url = meme["url"], meme_author = meme["author"])

app.run()  