import random
import math

class user:
    def __init__(self, v_cor):
        # x_axis value # y_axis value
        self.cor = v_cor
    
    def set_cov(self, v_cor):
        self.cor = v_cor
    
    def get_cor(self):
        return self.cor
        
    def move_right(self):
        if self.cor[1] < 20:
            self.cor[1] += 1
            return True
        else:
            return False

    def move_left(self):
        if self.cor[1] > 1:
            self.cor[1] -= 1
            return True
        else:
            return False
    
    def move_above(self):
        if self.cor[0] > 1:
            self.cor[0] -= 1
            return True
        else:
            return False

    def move_below(self):
        if self.cor[0] < 20:
            self.cor[0] += 1
            return True
        else:
            return False

    def set_goal(self, v_cor):
        self.desti = v_cor

    def get_goal(self):
        return self.desti

    def travel(self):
        if (self.cor[0] <= self.desti[0]) and (self.cor[1] <= self.desti[1]):
            if self.cor[0] == self.desti[0]:
                self.move_right()
                return
            if self.cor[1] == self.desti[1]:
                self.move_below()
                return
            if random.random() >= 0.5:
                self.move_below()
            else:
                self.move_right()
        if (self.cor[0] >= self.desti[0]) and (self.cor[1] >= self.desti[1]):
            if self.cor[0] == self.desti[0]:
                self.move_left()
                return
            if self.cor[1] == self.desti[1]:
                self.move_above()
                return
            if random.random() >= 0.5:
                self.move_above()
            else:
                self.move_left()
    
    def estimate(self, rssi_list):
        estimate_cor = [0, 0]
        estimate_grid = {}
        for i in range(1, 21):
            for j in range(1, 21):
                estimate_grid[(i, j)] = 0
        for beacon_info in rssi_list:
            if beacon_info[1] != 0:
                x = []
                y = []
                beacon_cor = beacon_info[0]
                est_distance = math.pow(math.e, -(beacon_info[1] + 35) / 17)
                for theta in range(0, 360, 15):
                    x.append(round(beacon_cor[0] + est_distance * math.cos(math.radians(theta))))
                    y.append(round(beacon_cor[1] + est_distance * math.sin(math.radians(theta))))
                for idx in range(len(x)):
                    if (1 <= x[idx]) and (x[idx] <= 20):
                        if (1 <= y[idx]) and (y[idx] <= 20):
                            estimate_grid[(x[idx], y[idx])] += 1
        prob_cor = 0
        for cor in estimate_grid.keys():
            if estimate_grid[cor] > prob_cor:
                prob_cor = estimate_grid[cor]
                estimate_cor = cor
        return estimate_cor
