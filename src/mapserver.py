import time

class map_server():
    def __init__(self, plana):
        self.plan = plana
        self.is_digging = False

    def display(self):
        for ligne in self.plan:
            for char in ligne:
                print(char+" ", end = '')
            print("")

    def get_crystal(self, x, y):
        self.plan[x][y] = '0'
        self.is_digging = False
