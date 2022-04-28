from src import truck, map
import sys


def mutiple_truck(map_id, text_name):
    carte, nbcamion, width, long = map.get_map(int(map_id), text_name)
    i = 0
    j = 0
    for i in range(len(carte)):
        for j in range(len(carte[i])):
            if carte[i][j] == " ":
                carte[i][j] = "0"
    for numcamion in range(nbcamion):

        x_min = int(len(carte) * numcamion / nbcamion)
        y_min = 0

        x_max = int(len(carte) * (numcamion + 1) / nbcamion)
        y_max = len(carte[0])

        print(y_max)
        truck1 = truck.truck(carte, numcamion, 0, numcamion)

        turn = truck1.get_path_to_destination(x_min, 0, 0, text_name)
        while True:
            x_dest, y_dest = truck1.recherch(x_min, y_min, x_max, y_max)
            if x_dest == -1:
                break
            turn = truck1.get_path_to_destination(x_dest, y_dest, turn, text_name)


map_id = str(sys.argv[1])
text_name = str(sys.argv[2])
mutiple_truck(map_id, text_name)
