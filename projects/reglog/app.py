from flask import Flask, request

app = Flask(__name__)

@app.get('/homepage')
def homepage():
    return "This is the homepage!"

@app.get('/test')
def test():
    return "This is a test"

@app.post('/login')
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    return "Login Successful!"