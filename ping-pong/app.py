from flask import Flask
import os

app = Flask(__name__)

PORT = os.getenv("PORT", "3000")

counter = 0

@app.route("/pingpong")
def pingpong():
    global counter
    response = f"pong {counter}"
    counter = counter + 1
    return response

app.run(host="0.0.0.0", port=int(PORT))