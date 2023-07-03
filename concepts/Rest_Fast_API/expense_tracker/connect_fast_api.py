
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import time

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
@app.route("/") # http://127.0.0.1:8000/
@app.get("/", response_class=HTMLResponse) # uvicorn connect_fast_api:app --reload
def login_page(request: Request):
    return templates.TemplateResponse("login_page.html", {"request": request})

@app.post("/login")
def login(request: Request, username: str, password: str):
    # Validate the username and password
    # Check if the credentials are valid in MongoDB
    # If valid, redirect to the account details page
    # If invalid, return an error message
    time.sleep(2)
    return RedirectResponse("/account_details") #{"message": "Login successful!"} # /account

@app.get("/account_details", response_class=HTMLResponse) # /account
def account_details(request: Request):
    # Retrieve the account details from MongoDB
    # Replace the dummy data with actual values from MongoDB
    username = "JohnDoe"
    balance = 1000
    return templates.TemplateResponse("main_page.html", {"request": request, "username": username, "balance": balance})

@app.post("/credit")
def credit(request: Request, amount: float):
    # Add the specified amount to the user's balance in MongoDB
    return {"message": "Amount credited successfully!"}

@app.post("/debit")
def debit(request: Request, amount: float):
    # Subtract the specified amount from the user's balance in MongoDB
    return {"message": "Amount debited successfully!"}

#app.run(host="0.0.0.0", port=80)


