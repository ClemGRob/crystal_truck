from shutil import move
import time
import threading
from mapserver import map_server

class truck(threading.Thread):

    def __init__(self, map, pos_x = 1, pos_y = 1):
        threading.Thread.__init__(self)
        self.x = pos_x
        self.y = pos_y
        self.score = 0
        self.map = map_server(map)

    def _move(self, value_x, value_y):
        self.x =value_x
        self.y =value_y
    def check_nearby_crystol(self, map):
        value = 0
        move = [self.x+1,self.y]
        if int(map[self.x+1][self.y])>value:
            value = int(map[self.x+1][self.y])
            move = [self.x+1,self.y]
        if int(map[self.x][self.y-1])>value:
            value = int(map[self.x][self.y-1])
            move = [self.x,self.y-1]
        if int(map[self.x-1][self.y])>value:
            value = int(map[self.x-1][self.y])
            move = [self.x-1,self.y]
        if int(map[self.x][self.y+1])>value:
            value = int(map[self.x][self.y+1])
            move = [self.x,self.y+1]
        self.score+=value

        print("move : "+str(move[0]))
        self.map.get_crystal(move[0], move[1])
        self._move(move[0], move[1])

    def run(self, map):
        while True:
            self.check_nearby_crystol(map)
            print("x : "+str(self.x)+", y : "+str(self.y))
            time.sleep(1)
            print(map.plan)



if __name__ == "__main__":
    thread1 = truck(1)
    thread1.start()

