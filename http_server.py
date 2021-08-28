from http.server import HTTPServer, BaseHTTPRequestHandler
import os
from main import main

# Create custom HTTPRequestHandler class

PORT = os.environ['PORT']
class KodeFunHTTPRequestHandler(BaseHTTPRequestHandler):

    # handle GET command
    def do_GET(self):
        try:
            if self.path.endswith('/new'):
                # send code 200 response
                self.send_response(200)
                msg = main().encode()

                # send header first
                self.send_header('Content-type', msg)
                self.end_headers()

                # send file content to client
                return

        except IOError:
            self.send_error(404, 'file not found')


def run():
    print('http server is starting...')

    # ip and port of servr
    # by default http server port is 80
    server_address = ('www.rotohands-bld-parser.herokuapp.com', int(PORT))
    httpd = HTTPServer(server_address, KodeFunHTTPRequestHandler)
    print('http server is running...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()