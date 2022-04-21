import game
import sys
import io
from contextlib import redirect_stdout

def get_ma_map():
    f = io.StringIO()
    with redirect_stdout(f):
        game.init_game(2)
    out = f.getvalue()
    lignes = out.split('\n')
    return lignes[5:-4]

# def get_map(map = "map.txt"):
#     f = open(map, "r")
#     carte = f.read()
#     lignes = carte.split('\n')
#     crystaux = []
#     i = 0
#     for ligne in lignes:
#         crystaux.insert(i, [char for char in ligne] )
#         i+=1
#     print(crystaux[1][1])
#     print(crystaux[1][2])
#     print(crystaux[1][3])
#     print(crystaux[1][4])
        

get_ma_map()