import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import threading
import os
PORT = os.environ['PORT']

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.write("Heroku is awesome")

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

try:
    server = ThreadedTCPServer(('', PORT), myHandler)
    print ('Started httpserver on port ' , PORT)
    ip,port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    allow_reuse_address = True
    server.serve_forever()

except KeyboardInterrupt:
    print ('CTRL + C RECEIVED - Shutting down the REST server')
    server.socket.close()