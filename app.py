from flask import Flask
import threading, time, subprocess

app = Flask(__name__)

def infinite_thread():
    while True:
        subprocess.run("python gitpod.py", shell=True)
        time.sleep(5)
        pass

@app.route('/gitpod')
def gitpod_route():
    thread = threading.Thread(target=infinite_thread)
    thread.daemon = True
    thread.start()
    return "Uptime Active"

@app.route('/')
def home():
    return "Miyan"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)