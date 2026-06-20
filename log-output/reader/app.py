from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    try:
        with open("/usr/src/app/files/output.txt", "r") as f:
            log_line = f.read()
        with open("/usr/src/app/files/pingpong.txt", "r") as f:
            pings = f.read()
        return f"<pre>{log_line}\nPing / Pongs: {pings}</pre>"
    except Exception as e:
        return f"No data yet: {e}"

app.run(host="0.0.0.0", port=3000)