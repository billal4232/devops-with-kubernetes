from flask import Flask, request, jsonify
import os
import psycopg2

app = Flask(__name__)

PORT = os.getenv("PORT", "3001")

def get_conn():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )

@app.route("/todos", methods=["GET"])
def get_todos():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT content FROM todos")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    todos = [row[0] for row in rows]
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def create_todo():
    new_todo = request.json["todo"]
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO todos (content) VALUES (%s)", (new_todo,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"todo": new_todo})
app.run(host="0.0.0.0", port=int(PORT))
