from flask import Flask, send_file, request, redirect
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
    todos = requests.get("http://todo-backend-svc:3005/todos").json()

    todo_items = ""
    for todo in todos:
        todo_items += f"<li>{todo}</li>"

    return f'''
    <html>
    <body style="text-align: center;">
        <h1>Todo App</h1>
        <img src="/image" style="width: 200px; border-radius: 10px;">
        <div>
            <form action="/new-todo" method="post">
                <input type="text" name="todo" maxlength="140" placeholder="Enter a new todo (max 140 characters)">
                <button type="submit">Send</button>
            </form>
        </div>
        <h2>Todos</h2>
        <ul style="list-style: none; display: inline-block; text-align: left;">
            {todo_items}
        </ul>
    </body>
    </html>
    '''

@app.route("/new-todo", methods=["POST"])
def new_todo():
    todo = request.form["todo"]
    requests.post("http://todo-backend-svc:3005/todos", json={"todo": todo})
    return redirect("/")

@app.route("/image")
def image():
    if not os.path.exists(IMAGE_PATH) or time.time() - os.path.getmtime(IMAGE_PATH) > 600:
        fetch_image()
    return send_file(IMAGE_PATH)

app.run(host="0.0.0.0", port=int(PORT))