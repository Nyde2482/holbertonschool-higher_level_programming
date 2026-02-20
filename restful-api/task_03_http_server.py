#!/usr/bin/python3
"""
Simple HTTP Server module.

This module creates a basic HTTP server that responds to GET requests
with different endpoints. The server runs on port 8000 and serves
both plain text and JSON responses.
"""
import http.server
import socketserver
import json
PORT = 8000


class Server(http.server.BaseHTTPRequestHandler):
    """
    HTTP request handler class.

    This class handles HTTP GET requests for different endpoints:
    - '/' returns a simple greeting message
    - '/data' returns JSON data
    - '/status' returns server status

    Inherits from BaseHTTPRequestHandler to provide HTTP functionality.
    """

    def do_GET(self):
        """
        Handle HTTP GET requests.

        Routes requests to different endpoints:
        - '/' : Returns a welcome message in plain text
        - '/data' : Returns JSON data with user information
        - '/status' : Returns server status as plain text

        Args:
            None

        Returns:
            None
        """
        if self.path == "/":

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":

            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode())

        elif self.path == "/status":

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":

            data = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            json_data = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode())

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


with socketserver.TCPServer(("", PORT), Server) as httpd:
    httpd.serve_forever()
