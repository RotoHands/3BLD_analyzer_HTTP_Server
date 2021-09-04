# -*- coding: utf-8 -*-
import http
from http.server import  BaseHTTPRequestHandler
from werkzeug import urls
import os
from BLD_Parser import parse_solve, parse_smart_cube_solve

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
    if cube.smart_cube:
        cube = parse_smart_cube_solve(cube)
    solve_str = cube.url
    return solve_str

class S(BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
            post_data = self.rfile.read(content_length)  # <--- Gets the data itself
            dict_params = urls.url_decode(post_data).to_dict()
            solve_str = parse(dict_params)

            self._set_response()
            self.wfile.write(bytearray((solve_str).encode('utf-8')))
        except Exception as e:
           self.send_error(404, 'error')


def run_http_server():
    PORT = os.environ['PORT']
    server_address = ('0.0.0.0', int(PORT))
    # server_address = ('127.0.0.1', 8080)
    httpd = http.server.HTTPServer(server_address, S)
    print('http server is running...')
    httpd.serve_forever()

def main():
    pass

if __name__ == '__main__':
    main()