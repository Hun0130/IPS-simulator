import math
import numpy
import random

class node:
    per = 0
    def __init__(self, v_cor):
        # x_axis value # y_axis value
        self.cor = v_cor
        self.channel_num = 11
        self.set_interfer(0)
        # random.seed()

    # set the channel number
    def set_channel(self, channel_n):
        # channel number
        self.channel_num = channel_n
        # random.seed()

    #   0, 5, 10, 20
    def set_interfer(self, intfer):
        self.interfer = intfer
        return 

    # get the channel number
    def get_channel(self):
        return self.channel_num
    
    # get the Coordinates
    def get_cor(self):
        return self.cor

    # get the distance between node and user
    def get_distance(self, cor_user):
        distance = 0
        distance += (cor_user[0]/2 - self.cor[0]/2) ** 2
        distance += (cor_user[1]/2 - self.cor[1]/2) ** 2
        distance = distance ** 0.5
        return distance

    # PL^_(d)[dBm] = PL^_(d0) + 10 * n log (d / d0)
    # PL(d) : N(PL^_, X_σ) where a Gaussian distributed random variable with zero mean and σ standard deviation (the units are dBm)
    # n is path loss exponent 
    # In building line-of-sight 1.6 to 1.8
    # free spac is 2, Obstructed in buildings 4 to 6, Obstructed in factories 2 to 3
    def generate_rssi(self, distance):
        # ple is different from channel and distance
        # random.seed(self.channel_num)
        # ple = path loss exponent
        ple = random.uniform(1.6, 1.8)
        standard_deviation = random.uniform(1, 2)
        rssi = -35 - 10 * ple * math.log10(distance+1) + numpy.random.normal(0, standard_deviation)
        return rssi

    # Table of Packetloss rate with Interferences
    #     WIFI 10Mbps  WIFI 20Mbps  No Interfer  WIFI 5Mbps   WIFI 50Mbps
    # 1m      4%           8%          0%           2%            90%
    # 2m      5%           10%         0%           3%            90%
    # 3m     30%           60%         5%           15%           99%
    # 4m     50%           90%         5%           35%           99%
    # 5m     45%           90%         5%           30%           ...
    # 6m     45%           90%         5%           30%
    # 7m     35%           90%         5%           25%
    # 8m     45%           90%         10%          35%
    # 9m     45%           90%         10%          35%
    # 10m    45%           90%         10%          35%
    # 11m    50%           90%         15%          40$
    # 12m    50%           90%         15%          40%
    # 13m    50%           90%         15%          40%
    # 14m    50%           90%         15%          40%
    # Lost Packet + Corrupt Packets = PER Rate
    # True = packet loss, False = no loss
    def packet_loss(self, distance):
        if 0 <= distance <= 1:
            if self.interfer == 0:
                return False
            if self.interfer == 5:
                if random.random() <= 0.02:
                    return True
                else:
                    return False
            if self.interfer == 10:
                if random.random() <= 0.04:
                    return True
                else:
                    return False
            if self.interfer == 20:
                if random.random() <= 0.08:
                    return True
                else:
                    return False
            if self.interfer == 50:
                if random.random() <= 0.9:
                    return True
                else:
                    return False
        if 1 <= distance < 2:
            if self.interfer == 0:
                return False
            if self.interfer == 5:
                if random.random() <= 0.03:
                    return True
                else:
                    return False
            if self.interfer == 10:
                if random.random() <= 0.05:
                    return True
                else:
                    return False
            if self.interfer == 20:
                if random.random() <= 0.1:
                    return True
                else:
                    return False
            if self.interfer == 50:
                if random.random() <= 0.9:
                    return True
                else:
                    return False
        if 2 <= distance < 3:
            if self.interfer == 0:
                if random.random() <= 0.05:
                    return True
                else:
                    return False
            if self.interfer == 5:
                if random.random() <= 0.15:
                    return True
                else:
                    return False
            if self.interfer == 10:
                if random.random() <= 0.3:
                    return True
                else:
                    return False
            if self.interfer == 20:
                if random.random() <= 0.6:
                    return True
                else:
                    return False
            if self.interfer == 50:
                if random.random() <= 0.99:
                    return True
                else:
                    return False
        if 3 <= distance < 4:
            if self.interfer == 0:
                if random.random() <= 0.05:
                    return True
                else:
                    return False
            if self.interfer == 5:
                if random.random() <= 0.35:
                    return True
                else:
                    return False
            if self.interfer == 10:
                if random.random() <= 0.5:
                    return True
                else:
                    return False
            if self.interfer == 20:
                if random.random() <= 0.9:
                    return True
                else:
                    return False
            if self.interfer == 50:
                if random.random() <= 0.99:
                    return True
                else:
                    return False
        if 4 <= distance < 5:
            if self.interfer == 0:
                if random.random() <= 0.05:
                    return True
                else:
                    return False
            if self.interfer == 5:
                if random.random() <= 0.3:
                    return True
                else:
                    return False
            if self.interfer == 10:
                if random.random() <= 0.45:
                    return True
                else:
                    return False
            if self.interfer == 20:
                if random.random() <= 0.9:
                    return True
                else:
                    return False
            if self.interfer == 50:
                if random.random() <= 0.99:
                    return True
                else:
                    return False
        if 5 <= distance < 7:
            if self.interfer == 0:
                if random.random() <= 0.05:
                    return True
                else:
                    return False
            if self.interfer == 5:
                if random.random() <= 0.3:
                    return True
                else:
                    return False
            if self.interfer == 10:
                if random.random() <= 0.45:
                    return True
                else:
                    return False
            if self.interfer == 20:
                if random.random() <= 0.9:
                    return True
                else:
                    return False
            if self.interfer == 50:
                if random.random() <= 0.99:
                    return True
                else:
                    return False
        if 7 <= distance < 8:
            if self.interfer == 0:
                if random.random() <= 0.05:
                    return True
                else:
                    return False
            if self.interfer == 5:
                if random.random() <= 0.25:
                    return True
                else:
                    return False
            if self.interfer == 10:
                if random.random() <= 0.35:
                    return True
                else:
                    return False
            if self.interfer == 20:
                if random.random() <= 0.9:
                    return True
                else:
                    return False
            if self.interfer == 50:
                if random.random() <= 0.99:
                    return True
                else:
                    return False
        if 8 <= distance < 11:
            if self.interfer == 0:
                if random.random() <= 0.1:
                    return True
                else:
                    return False
            if self.interfer == 5:
                if random.random() <= 0.35:
                    return True
                else:
                    return False
            if self.interfer == 10:
                if random.random() <= 0.45:
                    return True
                else:
                    return False
            if self.interfer == 20:
                if random.random() <= 0.9:
                    return True
                else:
                    return False
            if self.interfer == 50:
                if random.random() <= 0.99:
                    return True
                else:
                    return False
        if 11 <= distance < 15:
            if self.interfer == 0:
                if random.random() <= 0.15:
                    return True
                else:
                    return False
            if self.interfer == 5:
                if random.random() <= 0.4:
                    return True
                else:
                    return False
            if self.interfer == 10:
                if random.random() <= 0.5:
                    return True
                else:
                    return False
            if self.interfer == 20:
                if random.random() <= 0.9:
                    return True
                else:
                    return False
            if self.interfer == 50:
                if random.random() <= 0.99:
                    return True
                else:
                    return False
        return

    # beacon make a rssi value to user
    # If channel loss exist, return 0
    def beacon(self, cor_user):
        distance = self.get_distance(cor_user)
        if self.packet_loss(distance):
            return [self.cor, 0]
        else:
            return [self.cor, self.generate_rssi(distance)]

    # beacon make a rssi value to user
    # If channel loss exist, return 0
    def kalman_beacon(self, cor_user):
        distance = self.get_distance(cor_user)
        if self.packet_loss(distance):
            return [self.cor, 0]
        else:
            feedback_const = 0.5
            rssi_feedback = self.generate_rssi(distance)
            for i in range(3):
                rssi_feeback = feedback_const * self.generate_rssi(distance) + (1 - feedback_const) * rssi_feedback
            return [self.cor, rssi_feedback]
