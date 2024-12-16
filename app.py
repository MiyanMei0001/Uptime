from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World", 200

@app.route('/gitpod')
def gitpod():
    result = subprocess.check_output("python gitpod.py", shell=True, text=True)
    return result, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')