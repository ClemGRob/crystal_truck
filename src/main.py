from src import game, truck


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

        

map = get_map(18)
i = 0
j = 0
for i in range(len(map)) :
    for j in range(len(map[i])):
        if map[i][j]==' ':
            map[i][j]='0'

truck1 = truck.truck(map,5,5)

#truck1.check_nearby_crystol()
for i in range(200):
    x_dest, y_dest = truck1.recherch()
    if x_dest == -1:
        break
    truck1.get_path_to_destination(x_dest, y_dest)
    print("notre score est de : "+ str(truck1.score))
   

