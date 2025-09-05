import logging
import os
import socket  # Python - PC - Port communicate
import traceback

from flask import Flask, Response, request, send_file

app = Flask(__file__)

def getRandPort():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # INET = Internal Network
    sock.bind(("localhost", 0))
    port = sock.getsockname()[1]
    sock.close()
    return port

class WebServer(Flask):
    host = "localhost"
    port = getRandPort()

    # Singleton (single-use class)
    # __init__ -> self
    # __new__ -> class

    def __new__(cls):
        if hasattr(cls, "instance"): 
            return getattr(cls, "instance")
        
        self = super(cls, cls).__new__(cls)
        super(self.__class__, self).__init__(__name__)

        self.config["TRAP_HTTP_ECCEPTIONS"] = True

        @self.errorhandler(Exception) # add error handler
        def handle_error(error):
            if not hasattr(error, "code") or error.code//100 == 5: 
                logging.error(traceback.format_exc())
                return Response(repr(error), 500)
            return Response.force_type(error, request.environ)
        
        logging.info(f"Server Instance created on ({self.host}, {self.port})")

        cls.instance = self

        @self.route("/")
        def Home():
            return send_file(os.path.join("..", "assets", "index.html"))
        
        @self.route("/assets/<path:file>")
        def Display(file):
            return send_file(os.path.join("..", "assets", file)) 
        
        return cls.instance

    def __init__(self):
        if hasattr(self.__class__, "instance"): 
            return
        super(self.__class__, self).__init__(__name__)

# app.run(debug=True, host=WebServer.host, port=WebServer.port)