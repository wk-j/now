from http.server import BaseHTTPRequestHandler
from cowpy import cow


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_headers()
        message = cow.Cowacter().milk("Hello from Python from a ZEIT Now Serverless function")
        self.wfile.write(message.encode())
        return
