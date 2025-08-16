from flask import Flask, request, send_file
import socket # Python - PC - Port communicate
import os

app = Flask(__file__)

def getRandPort():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # INET = Internal Network
    sock.bind(("localhost", 0))
    port = sock.getsockname()[1]
    sock.close()
    return port

@app.route("/")
def Home():
    return send_file(os.path.join("assets", "index.html"))

# app.run(debug=True, host="localhost", port=getRandPort()) # 5000