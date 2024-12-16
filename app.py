from flask import Flask
import threading
import time
import subprocess
import requests
import asyncio

app = Flask(__name__)

async def run_gitpod_async():
    # Menjalankan gitpod.py dalam proses terpisah
    process = await asyncio.create_subprocess_shell(
        "python gitpod.py",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    await asyncio.sleep(30)  # Tunggu selama 30 detik
    await requests.get("https://uptime-puce.vercel.app/gitpod")

def run_gitpod():
    asyncio.run(run_gitpod_async())

@app.route('/')
def home():
    return "Miyan"

@app.route('/gitpod')
def gitpod():
    thread = threading.Thread(target=run_gitpod)
    thread.start()  # Memulai thread untuk menjalankan run_gitpod
    return "Miyan"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
