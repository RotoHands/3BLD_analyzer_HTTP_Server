# -*- coding: utf-8 -*-
import http
from http.server import  BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from werkzeug import urls

import os
import json
from main import parse
import simplejson
# Create custom HTTPRequestHandler class

# PORT = os.environ['PORT']
from dotenv import load_dotenv
import os
from BLD_Parser import parse_solve, parse_smart_cube_solve, parse_url
def init_env_var(dict_params):

    os.environ["SMART_CUBE"] = "True" if dict_params["SMART_CUBE"] == "True" else "False"
    os.environ["GEN_PARSED_TO_CUBEDB"] = "True" if dict_params["GEN_PARSED_TO_CUBEDB"] == "True" else "False"
    os.environ["NAME_OF_SOLVE"] = dict_params["NAME_OF_SOLVE"]
    os.environ["TIME_SOLVE"] = dict_params["TIME_SOLVE"]
    os.environ["COMMS_UNPARSED"] = "True" if dict_params["COMMS_UNPARSED"] == "True" else "False"
    os.environ["GEN_WITH_MOVE_COUNT"] = "True" if dict_params["GEN_WITH_MOVE_COUNT"] == "True" else "False"
    os.environ["DIFF_BETWEEN_ALGS"] = dict_params["DIFF_BETWEEN_ALGS"]
    os.environ["PARSE_TO_LETTER_PAIR"] = "True" if dict_params["PARSE_TO_LETTER_PAIR"] == "True" else "False"
    os.environ["GEN_WITH_MOVE_COUNT"] = "True" if dict_params["GEN_WITH_MOVE_COUNT"] == "True" else "False"
    os.environ["EDGES_BUFFER"] = dict_params["EDGES_BUFFER"]
    os.environ["CORNER_BUFFER"] = dict_params["CORNER_BUFFER"]
    os.environ["LETTER_PAIRS_DICT"] = dict_params["LETTER_PAIRS_DICT"]
    os.environ["SCRAMBLE"] = dict_params["SCRAMBLE"]
    os.environ["SOLVE"] = dict_params["SOLVE"]
    os.environ["MEMO"] = dict_params["MEMO"]


def parse(dict_params):
    init_env_var(dict_params)
    cube = parse_solve(dict_params["SCRAMBLE"], dict_params["SOLVE"])
    print("here 1")
    if cube.smart_cube:
        cube = parse_smart_cube_solve(cube)
        print("here 2")
    solve_str = cube.url
    return solve_str

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
        dict_params = urls.url_decode(post_data).to_dict()
        for k in dict_params.keys():
            print("{} : {}".format(dict_params.get(k), type(dict_params.get(k))))

        solve_str = parse(dict_params)
        print(solve_str)
        self._set_response()
        self.wfile.write((solve_str).encode('iso-8859-8'))


def run():
    print('http server is starting...')

    # ip and port of servr
    # by default http server port is 80
    # server_address = ('0.0.0.0', int(PORT))
    server_address = ('127.0.0.1', 8080)
    httpd = http.server.HTTPServer(server_address, S)
    print('http server is running...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()