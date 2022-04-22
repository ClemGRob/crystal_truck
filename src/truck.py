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
            return -1 * a
        return a

    def recherch(self, x_min=-1, y_min=-1, x_max=-1, y_max=-1):
        distance = 1000
        x_ref = -1
        y_ref = 0
        if y_max != -1:
            for j in range(y_min, y_max):
                for i in range(x_min, x_max):
                    print(str(i) + " " + str(j))
                    if self.map[i][j] != "0":
                        tmp_distance = self.abs_value(self.x - i) + self.abs_value(
                            self.y - j
                        )
                        if self.y > j:
                            tmp_distance -= self.y
                        if tmp_distance < distance:
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
                        if tmp_distance < distance:
                            distance = tmp_distance
                            x_ref = i
                            y_ref = j
        return x_ref, y_ref

    def get_path_to_destination(self, x_dest, y_dest, turn, text_name):
        local_turn = turn
        while self.y != y_dest or self.x != x_dest:

            if self.y < y_dest:
                local_turn += 1
                self.move_up(local_turn, text_name)
            if self.y > y_dest:
                local_turn += 1
                self.move_down(local_turn, text_name)
            if self.x < x_dest:
                local_turn += 1
                self.move_right(local_turn, text_name)
            if self.x > x_dest:
                local_turn += 1
                self.move_left(local_turn, text_name)
        local_turn += 1
        self.digg(local_turn, text_name)
        return local_turn

    def move_up(self, turn, text_name):
        self.y += 1
        self.write(turn, "MOVE", text_name)

    def move_down(self, turn, text_name):
        self.y -= 1
        self.write(turn, "MOVE", text_name)

    def move_left(self, turn, text_name):
        self.x -= 1
        self.write(turn, "MOVE", text_name)

    def move_right(self, turn, text_name):
        self.x += 1
        self.write(turn, "MOVE", text_name)

    def digg(self, turn, text_name):
        self.score += int(self.map[self.x][self.y])
        if self.map[self.x][self.y] == "2":
            self.map[self.x][self.y] = "1"
        else:
            self.map[self.x][self.y] = "0"
        self.write(turn=turn, action="DIG", name=text_name)

    def write(self, turn=0, action="MOVE", name="map.txt"):
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
            + "\n",
            name,
        )
