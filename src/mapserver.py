from time import time


import time
class map_server():
    def __init__(self, plan):
        self.plan = plan
        self.is_digging = False

    def get_crystal(self, x, y):
        # while True:
        #     if self.is_digging == False:
        #         self.is_digging = True
        #         break
        
        self.plan[x][y] = '0'
        


