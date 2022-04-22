from statistics import multimode
from src import truck, map


def mutiple_truck():
    carte, nbcamion, width, long = map.get_map(18)
    i = 0
    j = 0
    for i in range(len(carte)):
        for j in range(len(carte[i])):
            if carte[i][j] == " ":
                carte[i][j] = "0"
    for numcamion in range(nbcamion):
        print("nous en somes au camion : " + str(numcamion))
        x_min = int(len(carte) * numcamion / nbcamion)
        # x_min = int(len(carte) * (nbcamion-numcamion) / nbcamion)
        # x_max = int(len(carte) * (nbcamion-numcamion+1) / nbcamion)
        # print("x min :  "+str(x_min))
        # print("x max :  "+str(x_max))
        y_min = 0
        x_max = int(len(carte) * (numcamion + 1) / nbcamion)
        
        y_max = len(carte[0])

        print(y_max)
        truck1 = truck.truck(carte, numcamion, 0, numcamion)
        
        turn = truck1.get_path_to_destination(x_min, 0, 0)
        while True:
            x_dest, y_dest = truck1.recherch(x_min, y_min, x_max, y_max)
            if x_dest == -1:
                break
            turn = truck1.get_path_to_destination(x_dest, y_dest, turn)
mutiple_truck()
