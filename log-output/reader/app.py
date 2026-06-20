from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    try:
        with open("/usr/src/app/files/output.txt", "r") as f:
            content = f.read()
        return content
    except Exception as e:
        return f"No data yet: {e}"

app.run(host="0.0.0.0", port=3000)