import http.client
import json
import requests
import re

def load_letter_pairs_dict(path_letter_pair):
    """
    gets a text file with list of place in cube and its letter pair ("ULB" : "A").
    returns a dictionary object of { place : letter_pair }
    """

    with open(path_letter_pair, "r", encoding="utf-8") as f:
        dict_lp = {}
        file = f.readlines()
        for line in file:
            split_data = re.findall('"([^"]*)"', line)
            dict_lp[split_data[0]] = split_data[1]
    return (dict_lp)


with open("example_solves/example_smart_cube.txt", "r") as f:
    data = f.readlines()
    SCRAMBLE = data[0]
    SOLVE = " ".join(data[1:])

letter_pair_dict = load_letter_pairs_dict("sticker_HEB.txt")
memo_time = 23.23
params_solve = {"DIFF" : 0.89,
          "SMART_CUBE": True,
          "COMMS_UNPARSED" :False,
          "E_BUF" : "UF",
          "C_BUF" : "UFR",
          "LP": True ,
          "MOVE_COUNT" : True,
          "LETTER_PAIRS" : letter_pair_dict.__str__(),
          "CUBEDB" : True,
          "NAME_OF_SOLVE" : "example_smart_cube",
          "TIME_SOLVE" : 56.12,
          "SCRAMBLE" : SCRAMBLE,
          "SOLVE" : SOLVE,
          "MEMO" : memo_time
}
# r = requests.post("http://rotohands-bld-parser.herokuapp.com/", data=params_solve)
r = requests.post("127.0.0.1:8080", data=params_solve)
print(r.text)
