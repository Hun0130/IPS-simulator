import random
import math

# 유저 노드 객체 파일

class user:
    # 예측된 좌표 (기본값 편의상 (1,1)로)
    estimate_cor = (1,1)
    # 예측 에러값 저장 (적분된 절대값)
    integrated_error = 0
    # 예측 횟수를 저장
    estimate_num = 0
    # 패킷 로스의 평균
    packet_loss_average = 0
    # 패킷 로스 발생 횟수 (각 예측 시의)
    packet_loss_num = 0
    # 패킷 로스 발생 횟수 (전체 시뮬레이션의)
    all_packet_loss_num = 0

    # 유저 노드 생성자
    def __init__(self, v_cor):
        # (x 좌표 값, y좌표 값)
        self.cor = v_cor
    
    # 유저의 좌표를 설정
    def set_cov(self, v_cor):
        self.cor = v_cor
    
    # 유저의 좌표를 반환
    def get_cor(self):
        return self.cor
        
    # 유저 노드를 오른쪽으로 이동
    def move_right(self):
        if self.cor[1] < 20:
            self.cor[1] += 1
            return True
        else:
            return False

    # 유저 노드를 왼쪽으로 이동
    def move_left(self):
        if self.cor[1] > 1:
            self.cor[1] -= 1
            return True
        else:
            return False
    
    # 유저 노드를 위쪽으로 이동
    def move_above(self):
        if self.cor[0] > 1:
            self.cor[0] -= 1
            return True
        else:
            return False

    # 유저 노드를 아래쪽으로 이동
    def move_below(self):
        if self.cor[0] < 20:
            self.cor[0] += 1
            return True
        else:
            return False

    # 유저 노드의 목표 좌표를 설정
    def set_goal(self, v_cor):
        self.desti = v_cor

    # 유저 노드의 목표 좌표를 반환
    def get_goal(self):
        return self.desti

    # 유저 노드를 목표 좌표 방향으로 이동 시킴 (랜덤하게 이동)
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

    # 예측 좌표와 실제 좌표의 거리 차이를 반환
    def get_distance(self):
        distance = 0
        distance += (self.cor[0]/2 - self.estimate_cor[0]/2) ** 2
        distance += (self.cor[1]/2 - self.estimate_cor[1]/2) ** 2
        distance = distance ** 0.5
        return distance

    # RSSI 리스트를 통해 예측 좌표를 생성함
    # ================== 이 함수를 수정해서 예측 알고리즘을 변경 할 수 있음 ========================
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
                    # 여기서 18의 값은 ple_dist + ple_ch의 평균으로 Least Mean Squared 값을 사용했다고 가정함
                    est_distance = math.pow(10, -(beacon_info[1] + 35) / 18) - 1
                    theta_interval = 15
                    for theta in range(0, 360, theta_interval):
                        x.append(round(beacon_cor[0] + est_distance * math.cos(math.radians(theta))))
                        y.append(round(beacon_cor[1] + est_distance * math.sin(math.radians(theta))))
                    for idx in range(len(x)):
                        if (1 <= x[idx]) and (x[idx] <= 20) and (1 <= y[idx]) and (y[idx] <= 20):
                            estimate_grid[(x[idx], y[idx])] += (1 / (est_distance + 1))
                else:
                    self.packet_loss_num += 1
                    self.all_packet_loss_num += 1
            prob_cor = 0
            for cor in estimate_grid.keys():
                if estimate_grid[cor] > prob_cor:
                    prob_cor = estimate_grid[cor]
                    self.estimate_cor = cor
            return self.estimate_cor
        except:
            print("esti error")
            input()
    # =============================================================================================

    # 예측 좌표와 실제 좌표와의 차이 (에러)를 반환
    def error(self):
        self.integrated_error += self.get_distance()
        self.estimate_num += 1
        return self.get_distance()

    # 적분된 에러 값을 반환
    def intga_error(self):
        return self.integrated_error

    # 시뮬레이션 전체 평균 에러를 반환
    def whole_error(self):
        if self.estimate_num != 0:
            return self.integrated_error / self.estimate_num
        else:
            return 0

    # 각 예측시의 패킷 로스 수를 반환
    def packet_loss_each(self):
        return self.packet_loss_num

    # 시뮬레이션 전체 평균 패킷 로스를 반환
    def avg_packet_loss(self):
        return self.all_packet_loss_num / self.estimate_num
