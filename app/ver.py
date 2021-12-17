import datetime
import pymysql
from app import app
from db import mysql
from flask import jsonify


@app.route('/')
def users():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT VERSION();")
    rows = cursor.fetchall()

    resp = jsonify(rows)
    resp.status_code = 200

    return jsonify({"hello": "Flask/MySQL",
                    "version": rows,
                    "time": datetime.datetime.now()})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
