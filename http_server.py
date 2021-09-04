import http
from http.server import  BaseHTTPRequestHandler
import os
from main import parse

# Create custom HTTPRequestHandler class

# PORT = os.environ['PORT']

class S(BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_GET(self):
        try:

            # send code 200 response
            self.send_response(200)
            self.send_header('Content-type', "text/html")
            self.end_headers()
            self.wfile.write(parse().encode())#main().encode())
        except IOError:
            self.send_error(404, 'file not found')

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        print("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))


def run():
    print('http server is starting...')

    # ip and port of servr
    # by default http server port is 80
    server_address = ('0.0.0.0', int(PORT))
    server_address = ('127.0.0.1', 8080)
    httpd = http.server.HTTPServer(server_address, S)
    print('http server is running...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()