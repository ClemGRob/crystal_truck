from src import game, truck, mapserver


import sys
import io
import truck
from mapserver import map_server
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

        

map = get_map()
bigmap = mapserver.map_server(map)
i = 0
j = 0
for i in range(len(map)) :
    for j in range(len(map[i])):
        if map[i][j]==' ':
            map[i][j]='0'

bigmap.display()

truck1 = truck.truck(bigmap,5,5)
print(truck1.score)
truck1.check_nearby_crystol()
print(truck1.score)
print(truck1.x)
print(truck1.y)
bigmap.display()
# truck1.start()
