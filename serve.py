#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer

#HTTPRequestHandler class
class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):

        # send response status code
        self.send_response(200)

        #   send headers
        self.send_headers("Content-type", "text/html")
        self.end_headers()

        #   write message
        self.wfile.write(bytes("hello, world!", "utf8"))
        return

# configure server
port = 5000
server_address = ("127.0.0.1", port)
httpd = HTTPServer(server_address, HTTPServer_RequestHandler)

# run server
httpd.serve_forever()