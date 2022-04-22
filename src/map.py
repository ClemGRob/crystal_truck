from src import game
import sys
import io
from contextlib import redirect_stdout

def get_map(map_id = 4):
    f = io.StringIO()
    with redirect_stdout(f):
        game.init_game(map_id)
    out = f.getvalue()
    lignes = out.split('\n')
    new_lignes = lignes[5:-4]
    map = []
    i = 0
    for ligne in new_lignes:
        map.insert(i, [char for char in ligne] )
        i+=1
    return map

def get_map_from_txt(map = "map.txt"):
    f = open(map, "r")
    carte = f.read()
    lignes = carte.split('\n')
    crystaux = []
    i = 0
    for ligne in lignes:
        crystaux.insert(i, [char for char in ligne] )
        i+=1
    return crystaux[5:int(lignes[2][-2:])+5]
    # return lignes[2][-2:]