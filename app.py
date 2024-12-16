from flask import Flask
import requests, subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World", 200

@app.route('/gitpod')
def gitpod():
    from gitpod import response
    return f"{response.text}", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')