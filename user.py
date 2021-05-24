import random
import math

class user:
    estimate_cor = (1,1)
    integrated_error = 0
    error_num = 0
    packet_loss_average = 0
    all_packet_get = 0
    packet_loss_num = 0
    all_packet_loss_num = 0
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
        try:
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
        except:
            print("travle error")
            input()
    
    # get the distance between two esti_cor and real_cor
    def get_distance(self):
        distance = 0
        distance += (self.cor[0]/2 - self.estimate_cor[0]/2) ** 2
        distance += (self.cor[1]/2 - self.estimate_cor[1]/2) ** 2
        distance = distance ** 0.5
        return distance


    def estimate(self, rssi_list):
        self.packet_loss_num = 0
        try:
            estimate_grid = {}
            for i in range(1, 21):
                for j in range(1, 21):
                    estimate_grid[(i, j)] = 0
            for beacon_info in rssi_list:
                self.all_packet_get += 1
                if beacon_info[1] != 0:
                    x = []
                    y = []
                    beacon_cor = beacon_info[0]
                    est_distance = math.pow(10, -(beacon_info[1] + 35) / 18) - 1
                    theta_interval = 15
                    for theta in range(0, 360, theta_interval):
                        x.append(round(beacon_cor[0] + est_distance * math.cos(math.radians(theta))))
                        y.append(round(beacon_cor[1] + est_distance * math.sin(math.radians(theta))))
                    for idx in range(len(x)):
                        if (1 <= x[idx]) and (x[idx] <= 20) and (1 <= y[idx]) and (y[idx] <= 20):
                            estimate_grid[(x[idx], y[idx])] += (1 / (est_distance + 1))
                            #estimate_grid[(x[idx], y[idx])] += 1
                else:
                    self.packet_loss_num += 1
                    self.all_packet_loss_num += 1
            prob_cor = 0
            for cor in estimate_grid.keys():
                # print(cor, estimate_grid[cor])
                if estimate_grid[cor] > prob_cor:
                    prob_cor = estimate_grid[cor]
                    self.estimate_cor = cor
            return self.estimate_cor
        except:
            print("esti error")
            input()

    def error(self):
        self.integrated_error += self.get_distance()
        self.error_num += 1
        return self.get_distance()

    def intga_error(self):
        return self.integrated_error

    def whole_error(self):
        if self.error_num != 0:
            return self.integrated_error / self.error_num
        else:
            return 0

    def packet_loss_each(self):
        return self.packet_loss_num

    def avg_packet_loss(self):
        return self.all_packet_loss_num / self.all_packet_get
