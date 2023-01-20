#!/usr/bin/env python3
import http.server
import os
import socketserver

PORT: int = int(os.environ["PORT"])
LISTEN_IP: str = "0.0.0.0"


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = "index.html"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


Handler = MyHttpRequestHandler

with socketserver.TCPServer((LISTEN_IP, PORT), Handler) as httpd:
    print(f"Http Server Serving at http://{LISTEN_IP}:{PORT}")
    httpd.serve_forever()
