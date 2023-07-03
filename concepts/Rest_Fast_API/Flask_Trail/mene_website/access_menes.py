from flask import Flask, render_template
import os
import requests
import json 

app = Flask(__name__)

#@app.route("/home")  # path to put after url for working

def get_menes():  # refere -- https://github.com/D3vd/Meme_Api
    url = "https://meme-api.com/gimme"
    responce = json.loads(requests.request(url=url, method="get").text)
    large_menes = responce['preview'][-2]
    subreddit = responce['subreddit']
    return large_menes, subreddit

def index():
    menes, sub_reddit = get_menes()
    return render_template("mene_index.html") #, memes_img=menes, subreddit=sub_reddit)

def home():
    return render_template('mene_index.html')

#@app.route("/home")

app.run(host="0.0.0.0", port=80)  # http://192.168.1.108:80/
