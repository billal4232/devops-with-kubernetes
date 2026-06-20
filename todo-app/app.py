from flask import Flask, send_file
import os
import time
import requests

app = Flask(__name__)

PORT = os.getenv("PORT", "3000")
IMAGE_PATH = "/usr/src/app/files/image.jpg"

def fetch_image():
    response = requests.get("https://picsum.photos/1200")
    with open(IMAGE_PATH, "wb") as f:
        f.write(response.content)

@app.route("/")
def home():
    return '''
    <html>
    <body style="text-align: center;">
        <h1>Todo App</h1>
        <img src="/image" style="width: 200px; border-radius: 10px;">
        <div>
            <input type="text" maxlength="140" placeholder="Enter a new todo (max 140 characters)" style="width: 300px; padding: 8px;">
            <button style="padding: 8px;">Send</button>
        </div>
        <h2>Todos</h2>
        <ul style="list-style: none; text-align: left; display: inline-block; line-height: 2;">
            <li>Learn Kubernetes basics</li>
            <li>Deploy application to cluster</li>
            <li>Configure persistent volumes</li>
        </ul>
    </body>
    </html>
    '''

@app.route("/image")
def image():
    if not os.path.exists(IMAGE_PATH) or time.time() - os.path.getmtime(IMAGE_PATH) > 600:
        fetch_image()
    return send_file(IMAGE_PATH)

app.run(host="0.0.0.0", port=int(PORT))