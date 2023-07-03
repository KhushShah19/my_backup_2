
from flask import Flask
from pymongo.mongo_client import MongoClient


app = Flask(__name__)

#@app.route("/")  # path to put after url for working

def index():
    return "first flask working" 

mdb_url = "mongodb://localhost:27017/?serverSelectionTimeoutMS=5000&connectTimeoutMS=10000"
client = MongoClient(mdb_url)

try:
    client.admin.command('ping')
    print("bd connected successfully")
except Exception as e:
    print(e)

#app.run(host="0.0.0.0", port=500) 










