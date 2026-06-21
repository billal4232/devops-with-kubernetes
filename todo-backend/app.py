from flask import Flask, request, jsonify
import os

app = Flask(__name__)

PORT = os.getenv("PORT", "3001")

todos = []   # in-memory list, persists across requests

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def create_todo():
    new_todo = request.json["todo"]
    todos.append(new_todo)
    return jsonify(todos)

app.run(host="0.0.0.0", port=int(PORT))