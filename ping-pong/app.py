from flask import Flask
import os
import psycopg2

app = Flask(__name__)
PORT = os.getenv("PORT", "3000")

def get_conn():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )

@app.route("/")
def health():
    return "ok", 200

@app.route("/pingpong")
def pingpong():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE pingpong SET count = count + 1 RETURNING count")
    count = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return f"pong {count}"

@app.route("/pings")
def pings():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT count FROM pingpong")
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return str(count)

app.run(host="0.0.0.0", port=int(PORT))