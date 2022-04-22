from enum import Flag
from shutil import move
from src import file_tool


class truck:
    def __init__(self, map=None, pos_x=1, pos_y=1, id=0):
        self.x = pos_x
        self.y = pos_y
        self.score = 0
        self.map = map
        self.id = id

    def abs_value(self, a):
        if a < 0:
            return -1*a
        return a

    def recherch(self, x_min=-1, y_min=-1, x_max=-1, y_max=-1):
        distance = 1000
        x_ref = -1
        y_ref = 0
        flag = False
        if y_max != -1:
            for j in range(y_min, y_max):
                for i in range(x_min, x_max):
                    print(str(i) + " " + str(j))
                    if self.map[i][j] != "0":
                        tmp_distance = self.abs_value(self.x - i) + self.abs_value(
                            self.y - j
                        )
                        if self.y > j and flag ==False:
                            distance = tmp_distance
                            x_ref = i
                            y_ref = j
                            flag = True
                        if tmp_distance < distance and flag ==False:
                            distance = tmp_distance
                            x_ref = i
                            y_ref = j

        else:
            for i in range(0, len(self.map)):
                for j in range(0, len(self.map[i])):
                    if self.map[i][j] != "0":
                        tmp_distance = self.abs_value(self.x - i) + self.abs_value(
                            self.y - j
                        )
                        # print("distance : "+str(tmp_distance)+" x_ref : "+str(self.abs_value(self.x-i))+" y_ref "+str(self.abs_value(self.y-j)))
                        if tmp_distance < distance:
                            distance = tmp_distance
                            x_ref = i
                            y_ref = j
        # print("\nmeilleur : \ndistance : "+str(distance)+" x_ref : "+str(x_ref)+" y_ref "+str(y_ref))
        return x_ref, y_ref

    def get_path_to_destination(self, x_dest, y_dest, turn):
        local_turn = turn
        while self.y != y_dest or self.x != x_dest:

            if self.y < y_dest:
                local_turn += 1
                self.move_up(local_turn)
            if self.y > y_dest:
                local_turn += 1
                self.move_down(local_turn)
            if self.x < x_dest:
                local_turn += 1
                self.move_right(local_turn)
            if self.x > x_dest:
                local_turn += 1
                self.move_left(local_turn)
        local_turn += 1
        self.digg(local_turn)
        return local_turn

    def move_up(self, turn):
        self.y += 1
        self.wright(turn)

    def move_down(self, turn):
        self.y -= 1
        self.wright(turn)

    def move_left(self, turn):
        self.x -= 1
        self.wright(turn)

    def move_right(self, turn):
        self.x += 1
        self.wright(turn)

    def digg(self, turn):
        self.score += int(self.map[self.x][self.y])
        if self.map[self.x][self.y] == "2":
            self.map[self.x][self.y] = "1"
        else:
            self.map[self.x][self.y] = "0"
        self.wright(turn=turn, action="DIG")

    def wright(self, turn=0, action="MOVE", name = "map.txt"):
        file_tool.write_new_line(
            str(turn)
            + " "
            + action
            + " "
            + str(self.id)
            + " "
            + str(self.y)
            + " "
            + str(self.x)
            + "\n"
            ,name
        )


# if __name__ == "__main__":
#     truck1 = truck(bigmap,5,5)
#     truck1.check_nearby_crystol()
#     for i in range(200):
#         x_dest, y_dest = truck1.recherch()
#         truck1.get_path_to_destination(x_dest, y_dest)
#         print("notre scor est de : "+ str(truck1.score))