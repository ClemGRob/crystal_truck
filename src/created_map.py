out = ["trucks: 4","width: 22","height: 13"]

# Program to write to text file using write() function
with  open("map_bis.txt", "w") as file:
	content = "%s" % out, "\n"
	file.writelines(content)
	file.close()

nbre_tours = 2
actions = "move"
ID_truck = 2
coordo_X = 0
coordo_Y = 1

add_nbr_tour = "%s" % nbre_tours,
add_action = " %d" % actions,
add_truck = " %s" % ID_truck,
add_X = " %s" % coordo_X,
add_Y =  " %s"% coordo_Y
with open('map_bis.txt', 'a') as f:
    f.writelines('\n'.join(add_nbr_tour,add_action,add_truck, add_X,add_y))

# Program to read the entire file (absolute path) using read() function
with open("map_bis.txt", "r") as file:
	content = file.read()
	print(content)
	file.close()