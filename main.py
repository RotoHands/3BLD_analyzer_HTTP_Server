from dotenv import load_dotenv
import os
from BLD_Parser import parse_solve, parse_smart_cube_solve, parse_url



def parse(dict_params):

    cube = parse_solve(SCRAMBLE, SOLVE)
    if cube.smart_cube:
        cube = parse_smart_cube_solve(cube)
    solve_str = cube.url
    return solve_str


if __name__ == '__main__':
    parse()
