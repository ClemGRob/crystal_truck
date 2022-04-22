from src import file_tool, game, truck, map


carte, a = map.get_map(18)


i = 0
j = 0
for i in range(len(carte)):
    for j in range(len(carte[i])):
        if carte[i][j] == " ":
            carte[i][j] = "0"

truck1 = truck.truck(carte, 0, 0)

# truck1.check_nearby_crystol()
turn = 0
for i in range(200):
    x_dest, y_dest = truck1.recherch()
    if x_dest == -1:
        break
    turn = truck1.get_path_to_destination(x_dest, y_dest, turn)
    print("notre score est de : " + str(truck1.score))
