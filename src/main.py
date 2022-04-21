from src import game,truck,map,mapserver
from mapserver import map_server
import sys
import io

from contextlib import redirect_stdout

def get_map():
    f = io.StringIO()
    with redirect_stdout(f):
        game.init_game(2)
    out = f.getvalue()
    lignes = out.split('\n')
    new_lignes = lignes[5:-4]
    map = []
    i = 0
    for ligne in new_lignes:
        map.insert(i, [char for char in ligne] )
        i+=1
    return map

#     print(crystaux[1][1])
#     print(crystaux[1][2])
#     print(crystaux[1][3])
#     print(crystaux[1][4])
        

map = get_map()
bigmap = map_server(map)
i = 0
j = 0
for i in range(len(map)) :
    for j in range(len(map[i])):
        if map[i][j]==' ':
            map[i][j]='0'

# print(bigmap.plan)
bigmap.get_crystal(0,1)
print(bigmap.plan)

truck1 = truck.truck(bigmap,5,5)


truck1.run(map)
