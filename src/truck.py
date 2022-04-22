# from shutil import move

class truck():

    def __init__(self, map, pos_x = 1, pos_y = 1, id = 0):
        # threading.Thread.__init__(self)
        self.x = pos_x
        self.y = pos_y
        self.score = 0
        self.map = map
        self.id = id

    def _move(self, value_x, value_y):
        self.x =value_x
        self.y =value_y

    def check_nearby_crystol(self):
        value = 0
        move = [self.x+1,self.y]
        if int(self.map[self.x+1][self.y])>value:
            value = int(self.map[self.x+1][self.y])
            move = [self.x+1,self.y]
        if int(self.map[self.x][self.y-1])>value:
            value = int(self.map[self.x][self.y-1])
            move = [self.x,self.y-1]
        if int(self.map[self.x-1][self.y])>value:
            value = int(self.map[self.x-1][self.y])
            move = [self.x-1,self.y]
        if int(self.map[self.x][self.y+1])>value:
            value = int(self.map[self.x][self.y+1])
            move = [self.x,self.y+1]
        self.score += value
        self.map.get_crystal(move[0], move[1])     
        self._move(move[0], move[1])

    def abs_value(self, i):
        if i > 0 : 
            return i
        return -1 * i


    def recherch(self):
        distance = 1000
        x_ref = -1
        y_ref = 0
        for i in range(0,len(self.map)):
            for j in range(0,len(self.map[i])):
                if self.map[i][j]!='0':
                    tmp_distance = self.abs_value(self.x-i)+self.abs_value(self.y-j)
                    #print("distance : "+str(tmp_distance)+" x_ref : "+str(self.abs_value(self.x-i))+" y_ref "+str(self.abs_value(self.y-j)))
                    if tmp_distance < distance:
                        distance = tmp_distance
                        x_ref = i
                        y_ref = j
        print("\nmeilleur : \ndistance : "+str(distance)+" x_ref : "+str(x_ref)+" y_ref "+str(y_ref))
        return x_ref, y_ref
    
    def get_path_to_destination(self, x_dest, y_dest):
        while self.y != y_dest or self.x != x_dest:
            if self.y < y_dest:
                self.move_up()
            if self.y > y_dest:
                self.move_down()
            if self.x < x_dest:
                self.move_right()
            if self.x > x_dest:
                self.move_left()
        self.digg()

    def move_up(self):
        self.y+=1
        self.wright()
    
    def move_down(self):
        self.y-=1
        self.wright()
    
    def move_left(self):
        self.x-=1
        self.wright()
    
    def move_right(self):
        self.x +=1
        self.wright()

    def digg(self):
        self.score+=int(self.map[self.x][self.y])
        self.map[self.x][self.y]='0'
        self.wright(action = "DIGG")
    
    def wright(self,action="MOVE"):
        print(action)
        pass

if __name__ == "__main__":
    truck1 = truck(bigmap,5,5)
    truck1.check_nearby_crystol()
    for i in range(200):
        x_dest, y_dest = truck1.recherch()
        truck1.get_path_to_destination(x_dest, y_dest)
        print("notre scor est de : "+ str(truck1.score))
   


