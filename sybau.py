# doxxing_tool.py
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    ip = request.remote_addr
    with open('ips.txt', 'a') as f:
        f.write(ip + '\n')
    return 'Your IP has been logged!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)