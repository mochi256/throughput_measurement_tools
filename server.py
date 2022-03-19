#!/usr/bin/env python3
import json
import threading
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from http import HTTPStatus
from datetime import datetime
import os

LOCK = threading.Lock()

PORT = int(os.environ["APP_SERVER_PORT"])
COUNT_MAX = int(os.environ["APP_COUNT_MAX"])
COUNT = 0

def httpServe():
    handler = StubHttpRequestHandler
    httpd = HTTPServer(('', PORT), handler)
    httpd.serve_forever()

class StubHttpRequestHandler(BaseHTTPRequestHandler):
    server_version = "HTTP Stub/0.1"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __send(self, data, status):
        data = json.dumps(data).encode()
        self.send_response(status)
        # specify json for content-type violate 
        # the cors policy, use text
        self.send_header("Content-type", "text/plain; charset=UTF-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Request-Headers", "Content-Type")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path != '/':
            self.__send({}, HTTPStatus.NOT_FOUND)
            return

        global COUNT
        if COUNT >= COUNT_MAX:
            print("[{0}] response null".format(
                datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f")
            ))
            self.__send({"number": None}, HTTPStatus.FORBIDDEN)
            return

        with LOCK:
            COUNT += 1
        print("[{0}] response {1}".format(
            datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f"),
            COUNT,
        ))
        self.__send({"number": COUNT}, HTTPStatus.OK)

if __name__ == "__main__":
    print('[{0}] server_start 0.0.0.0:{1}'.format(
        datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f"),
        PORT
    ))
    thread = threading.Thread(target=httpServe)
    thread.start()
