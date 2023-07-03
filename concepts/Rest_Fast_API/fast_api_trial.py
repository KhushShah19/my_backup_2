# pip install uvicorn gunicorn fastapi pydantic sklearn pandas

from fastapi import FastAPI
from pydantic import BaseModel

api_app = FastAPI()

# 
# to run: enter file name (normal way)
#
# Verify it is running (in Postman)
#   POST --> Body --> Raw --> Json (in Postman)
#   {
#    "Name": "raj",
#    "Age": 21,
#    "place": "mumbai",
#    "salary": 2000
#   }
#
# know if uvicorn server is working in background or not
# you can stop it with terminal (any changes to code might restart it)
#



class first_api(BaseModel):
    Name: str
    Age: int
    place: str
    salary: int

@api_app.post('/')

async def scroing_endpoint(item:first_api):
    return item

