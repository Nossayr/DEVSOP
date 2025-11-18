from flask import Flask, Response
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Métrique custom : Compteur de requêtes
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')

@app.route('/')
def hello():
    REQUEST_COUNT.inc()
    return "Hello, DevSecOps World!"

@app.route('/api/data')
def data():
    REQUEST_COUNT.inc()
    return {"status": "secure", "data": [1, 2, 3]}

# Endpoint pour Prometheus (Monitoring)
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)