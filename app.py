from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/db-test")
def db_test():
    try:
        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("SELECT DATABASE()")
        database_name = cursor.fetchone()[0]

        cursor.close()
        db.close()

        return jsonify({
            "success": True,
            "message": "Database Connected Successfully",
            "database": database_name
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Database Connection Failed",
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)