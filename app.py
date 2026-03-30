from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello, DevOps!"})

@app.route('/info')
def info():
    return jsonify({
        "version": "1.0.0",
        "author": "Іващук Святослав Андрійович"
    })
@app.route('/api/health')
def health():
    return jsonify({
        "healthy": True,
        "uptime": "24h",
        "service": "ShopEasy",
        "checkedBy": "s.ivashchuk"
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
