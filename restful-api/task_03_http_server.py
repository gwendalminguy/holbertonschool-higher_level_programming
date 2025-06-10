#!/usr/bin/python3
"""
Module containing class FirstServer.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class FirstServer(BaseHTTPRequestHandler):
    """
    A class to define a simple server.
    """
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            message = "Hello, this is a simple API!"
            self.wfile.write(bytes(message, "utf8"))
        
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.wfile.write(bytes(data, "utf8"))
            
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            message = "OK"
            self.wfile.write(bytes(message, "utf8"))

        else:
            self.send_response(404, message="Not Found")
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            message = "Endpoint not found"
            self.wfile.write(bytes(message, "utf8"))


def main():
    with HTTPServer(("", 8000), FirstServer) as server:
        server.serve_forever()


if __name__ == "__main__":
    main()
