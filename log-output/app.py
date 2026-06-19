from flask import Flask
import uuid
from datetime import datetime
import time
import threading

app = Flask(__name__)

random_string = str(uuid.uuid4())

def log_loop():
    while True:
        now = datetime.now()
        print(f"{now}: {random_string}")
        time.sleep(5)

threading.Thread(target=log_loop, daemon=True).start()

@app.route("/")
def home():
    now = datetime.now()
    return f"{now}: {random_string}"

app.run(host="0.0.0.0", port=3000)