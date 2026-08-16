"""
Tiny HTTP app used by the Docker lab (exam 4.6, 4.7).
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"CCNAAUTO docker lab. HOSTNAME={os.uname().nodename if hasattr(os, 'uname') else os.getenv('COMPUTERNAME')}\n"
        payload = body.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()
