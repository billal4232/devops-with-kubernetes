from flask import Flask
import requests
import os                          

app = Flask(__name__)

MESSAGE = os.getenv("MESSAGE")     

@app.route("/")
def home():
    try:
        with open("/usr/src/app/files/output.txt", "r") as f:
            log_line = f.read()
        
        with open("/usr/src/app/config/information.txt", "r") as f:   
            file_content = f.read()
        
        pings = requests.get("http://ping-pong-svc:3003/pings").text
        
        return f"<pre>file content: {file_content}\nenv variable: MESSAGE={MESSAGE}\n{log_line}\nPing / Pongs: {pings}</pre>"
    except Exception as e:
        return f"No data yet: {e}"

app.run(host="0.0.0.0", port=3000)