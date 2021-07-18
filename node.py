import math
import numpy
import random

# 센서 노드 객체 파일

class node:
    # 패킷 로스율 값
    per = 0
    # 패킷 로스 익스포넌트 값 (채널에 따른 값)
    ple_ch = 0

    # 노드 객체 생성자 (좌표와 ple seed)
    def __init__(self, v_cor, ple_seed):
        # x 축 좌표 값과 y 축 좌표 값
        self.cor = v_cor
        # 기본 채널은 11번
        self.channel_num = 11
        # 기본 채널 간섭은 0Mbps
        self.set_interfer(0)
        # ple 값은 ple seed
        self.ple_ch = ple_seed

    # 노드의 채널을 channel_n로 세팅
    def set_channel(self, channel_n, ple_seed):
        self.channel_num = channel_n
        self.ple_ch = ple_seed

    # 채널 간섭을 0, 5, 10, 20 Mbps 중 하나로 결정
    def set_interfer(self, intfer):
        self.interfer = intfer
        return 

    # 채널 수를 반환
    def get_channel(self):
        return self.channel_num
    
    # 센서 노드의 좌표를 반환
    def get_cor(self):
        return self.cor

    # 노드와 유저 사이의 거리를 반환
    def get_distance(self, cor_user):
        distance = 0
        distance += (cor_user[0]/2 - self.cor[0]/2) ** 2
        distance += (cor_user[1]/2 - self.cor[1]/2) ** 2
        distance = distance ** 0.5
        return distance

    # 노드에서 RSSI 값을 생성 (사용자와의 거리와 PLE값을 통해서 계산됨)
    # RSSI 값은 논문에서 구한 RSSI 모델링 식을 통해서 역생산됨
    # PL^_(d)[dBm] = PL^_(d0) + 10 * n log (d / d0)
    # PL(d) : N(PL^_, X_σ) where a Gaussian distributed random variable with zero mean and σ standard deviation (the units are dBm)
    # n is path loss exponent 
    # In building line-of-sight 1.6 to 1.8
    # free spac is 2, Obstructed in buildings 4 to 6, Obstructed in factories 2 to 3
    def generate_rssi(self, distance):
        # ple is different from channel and distance
        # random.seed(self.channel_num)
        # ple = path loss exponent
        # 1.6 ~ 1.8

        # 거리에 따른 ple 값도 랜덤하게 분포함
        ple_dist = random.uniform(0.6, 1.0)
        standard_deviation = random.uniform(1, 2)
        rssi = -35 - 10 * (ple_dist + self.ple_ch) * math.log10(distance+1) + numpy.random.normal(0, standard_deviation)
        return rssi

    # 거리와 간섭정도에 따른 패킷로스를 걱정
    # 패킷 로스율은 논문에 제공된 데이터를 사용
    # Table of Packetloss rate with Interferences
    #     WIFI 10Mbps  WIFI 20Mbps  No Interfer  WIFI 5Mbps   WIFI 50Mbps
    # 1m      4%           8%          0%           2%            20%
    # 2m      5%           10%         0%           3%            50%
    # 3m     30%           60%         5%           15%           90%
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
                if random.random() <= 0.2:
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
                if random.random() <= 0.5:
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
                if random.random() <= 0.9:
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

        return

    # RSSI 데이터를 생성해서 뿌려줌
    # 패킷 로스가 잃어나면, 0을 반환함
    def beacon(self, cor_user):
        distance = self.get_distance(cor_user)
        if self.packet_loss(distance):
            return [self.cor, 0]
        else:
            return [self.cor, self.generate_rssi(distance)]

    # RSSI 데이터를 생성해서 뿌려줌 (칼만필터 적용)
    # 패킷 로스가 잃어나면, 0을 반환함
    def kalman_beacon(self, cor_user):
        distance = self.get_distance(cor_user)
        if self.packet_loss(distance):
            return [self.cor, 0]
        else:
            feedback_const = 0.4
            rssi_feedback = self.generate_rssi(distance)
            for i in range(3):
                rssi_feedback = feedback_const * self.generate_rssi(distance) + (1 - feedback_const) * rssi_feedback
            return [self.cor, rssi_feedback]


    def beacon_100(self, cor_user):
        rssi_value = 0
        distance = self.get_distance(cor_user)
        for i in range(100):
            rssi_value += self.generate_rssi(distance)
        rssi_value = rssi_value / 100
        return rssi_value

