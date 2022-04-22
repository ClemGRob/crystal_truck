from src import game, truck, map






# tuttut = truck.truck(None, 1, 1)
# tuttut.move_down()
# print(tuttut.y)

print(map.get_map_from_txt())
map = map.get_map(18)
print("\n\n\n")
print(map)



# i = 0
# j = 0
# for i in range(len(map)) :
#     for j in range(len(map[i])):
#         if map[i][j]==' ':
#             map[i][j]='0'

# truck1 = truck.truck(map,5,5)

# #truck1.check_nearby_crystol()
# for i in range(200):
#     x_dest, y_dest = truck1.recherch()
#     if x_dest == -1:
#         break
#     truck1.get_path_to_destination(x_dest, y_dest)
#     print("notre score est de : "+ str(truck1.score))
   

