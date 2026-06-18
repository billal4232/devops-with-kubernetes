from flask import Flask
import os

app = Flask(__name__)

PORT = os.getenv("PORT", "3000")

print(f"Server started in port {PORT}")
app.run(host="0.0.0.0", port=int(PORT))