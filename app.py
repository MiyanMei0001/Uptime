from flask import Flask
import threading, time, subprocess, requests

app = Flask(__name__)

def run_gitpod():
    subprocess.run("python gitpod.py", shell=True)
    time.sleep(30)
    requests.get("https://uptime-chi.vercel.app/gitpod")

@app.route('/')
def home():
    return "Miyan"

@app.route('/gitpod')
def gitpod():
    run_gitpod()
    return "Miyan"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)