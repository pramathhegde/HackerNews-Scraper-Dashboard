from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

app = Flask(__name__)
CORS(app)

def fetch_headlines():
    conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, link, scraped_at FROM headlines ORDER BY scraped_at DESC LIMIT 20")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "title": r[1], "link": r[2], "scraped_at": str(r[3])} for r in rows]

@app.route("/api/headlines", methods=["GET"])
def get_headlines():
    return jsonify(fetch_headlines())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
