from flask import Flask

app = Flask(__name__)

@app.route("/")  # path to put after url for working

def index():
    return "first flask working" 


app.run(host="0.0.0.0", port=500) # run the code and filw while be up in running


