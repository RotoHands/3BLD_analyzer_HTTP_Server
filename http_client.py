import requests
import re

# this is an example of how a client request can be

def client_example():
    with open("example_solves/example_smart_cube.txt", "r") as f:
        data = f.readlines()
        SCRAMBLE = data[0]
        SOLVE = " ".join(data[1:])
    letter_pair_dict = load_letter_pairs_dict("sticker_letter_pairs.txt")
    params_solve = { "DIFF_BETWEEN_ALGS" : 0.89,
              "SMART_CUBE": True,
              "COMMS_UNPARSED" :False,
              "EDGES_BUFFER" : "UF",
              "CORNER_BUFFER" : "UFR",
              "PARSE_TO_LETTER_PAIR": True ,
              "GEN_WITH_MOVE_COUNT" : True,
              "LETTER_PAIRS_DICT" : letter_pair_dict.__str__(),
              "GEN_PARSED_TO_CUBEDB" : True,
              "NAME_OF_SOLVE" : "example_smart_cube",
              "TIME_SOLVE" : 56.12,
              "SCRAMBLE" : SCRAMBLE,
              "SOLVE" : SOLVE,
              "MEMO" : 23.32
    }

    # r = requests.post("http://rotohands-bld-parser.herokuapp.com/", data=params_solve)
    r = requests.post("http://127.0.0.1:8080", data=params_solve)
    import pyperclip
    pyperclip.copy(r.text)


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

def main():
    client_example()

if __name__ == '__main__':
    main()