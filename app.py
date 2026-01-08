from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
counter = Counter('app_requests_total', 'Total Requests')

@app.route('/')
def home():
    counter.inc()
    return "Hello from Kubernetes + CI/CD"

@app.route('/metrics')
def metrics():
    return generate_latest()

app.run(host='0.0.0.0', port=5000)
