from shutil import move
import threading
import mapserver

class truck(threading.Thread):
    def __init__(self, pos_x, pos_y):
        threading.Thread.__init__(self)
        self.x = pos_x
        self.y = pos_y
        self.score = 0

    def move(self, value_x, value_y):
        self.x +=value_x
        self.y +=value_y
    def check_nearby_crystol(self, map):
        value = 0
        move = ""
        if map[self.x+1][self.y]>value:
            value = map[self.x+1][self.y]
            move = [self.x+1][self.y]
        if map[self.x][self.y-1]>value:
            value = map[self.x+1][self.y]
            move = [self.x+1][self.y]
        if map[self.x-1][self.y]>value:
            value = map[self.x+1][self.y]
            move = [self.x+1][self.y]
        if map[self.x][self.y+1]>value:
        if 
            value = map[self.x+1][self.y]
            move = [self.x+1][self.y]

        self.score+=value

            


    def run(self):
        while True:
            print(" Value send", self.h)

thread1 = mythread(1)

thread1.start()

