import http
from http.server import  BaseHTTPRequestHandler
import os
from main import main

# Create custom HTTPRequestHandler class

PORT = os.environ['PORT']

class KodeFunHTTPRequestHandler(BaseHTTPRequestHandler):

    # handle GET command
    def do_GET(self):
        try:

            # send code 200 response
            self.send_response(200)
            self.send_header('Content-type', "text/html")
            self.end_headers()
            self.wfile.write(main().encode())#main().encode())
        except IOError:
            self.send_error(404, 'file not found')


def run():
    print('http server is starting...')

    # ip and port of servr
    # by default http server port is 80
    server_address = ('0.0.0.0', int(PORT))
    httpd = http.server.HTTPServer(server_address, KodeFunHTTPRequestHandler)
    print('http server is running...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()