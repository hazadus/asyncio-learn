"""
Приложение Flask для выборки торговых марок

Running using Gunicorn:
gunicorn -w 8 ch9.listing_9_5:app

Load testing:
brew install wrk
wrk -c200 -t1 -d30 http://127.0.0.1:8000/brands

Test results:
Running 30s test @ http://127.0.0.1:8000/brands
  1 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    40.08ms    9.08ms  83.09ms   90.38%
    Req/Sec     2.78k     1.15k    3.58k    85.45%
  15315 requests in 30.08s, 229.12MB read
  Socket errors: connect 0, read 1083, write 441, timeout 0
Requests/sec:    509.12
Transfer/sec:      7.62MB
"""
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)
connection_info = "dbname=products user=postgres password=postgres host=127.0.0.1"
db = psycopg2.connect(connection_info)


@app.route("/brands")
def brands():
    cur = db.cursor()
    cur.execute("SELECT brand_id, brand_name FROM brand")
    rows = cur.fetchall()
    cur.close()
    return jsonify([{"brand_id": row[0], "brand_name": row[1]} for row in rows])
