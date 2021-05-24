import os
from typing import ChainMap
import node as nodeset
import user as us
import random

class system:
    def __init__(self):
        # use for check to update graphic
        self.check = True
        
        # number of sensor nodes
        self.node_num = 0
        
        # user node
        self.user =  us.user((0, 0))
        
        # the list of the channel used now
        self.channel_list = {}
        for i in range(11, 27):
            self.channel_list[i] = []
        
        # the level of Interference
        self.interference_level = {}
        for i in range(11, 27):
            self.interference_level[i] = 0
        
        # grid_map information
        self.grid_map = {}
        for i in range(1, 21):
            for j in range(1, 21):
                self.grid_map[(i,j)] = 0
        
        # user grid information
        self.user_grid = {}
        for i in range(1, 21):
            for j in range(1, 21):
                self.user_grid[(i,j)]= 0
        
        # estimation grid information
        self.esti_grid = {}
        for i in range(1, 21):
            for j in range(1, 21):
                self.esti_grid[(i,j)] = 0

        # check is in simulating
        self.in_simul = False

        # random seed for packet loss exponent by channel
        self.ple_seed ={}
        for i in range(11,27):
            self.ple_seed[i] = random.uniform(0.6, 1.4)

    # update the node info
    def update(self):
        for i in range(11, 27):
            self.channel_list[i] = []
        for cov_v in self.grid_map.keys():
            if self.grid_map[cov_v] != 0:
                node = self.grid_map[cov_v]
                if node.get_cor() not in self.channel_list[node.get_channel()]:
                    self.channel_list[node.get_channel()].append(node.get_cor())
        return

    # erase consol graphic
    def clear(self):
        if self.check == True:
            os.system('clear')
        return

    # Center Alignment Output
    def simul_print(self, string):
        print("{:^100}".format(string))
        return

    # print grid
    def print_grid(self):
        try:
            if self.check == True:
                self.simul_print("Indoor Localization Simulator\n")
                self.simul_print(" 1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20 ")
                self.simul_print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
                printed_ch = []
                for i in range(1, 21):
                    grid__input = str(i) + " |"
                    for key in self.grid_map.keys():
                        if key[0] == i:
                            if self.grid_map[key] != 0:
                                grid__input += "S"
                            if not self.grid_map[key] != 0:
                                grid__input += " "
                            if self.user_grid[key] != 0:
                                grid__input += "R"
                            if not self.user_grid[key] != 0:
                                grid__input += " "
                            if self.esti_grid[key] != 0:
                                grid__input += "E"
                            if not self.esti_grid[key] != 0:
                                grid__input += " "
                            grid__input += "|"
                    if i < 10:
                        grid__input += "  "
                    else:
                        grid__input += "   "
                    self.simul_print(grid__input)
                    print("         |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|", end='  ') 
                    if i == 1:
                        print("Sensor node: ", self.node_num, end='')
                    if i == 2:
                        print("Channel State: ", end = '')
                        for ch in self.channel_list.keys():
                            if (self.channel_list[ch] != []):
                                print(len(self.channel_list[ch])," nodes in ",ch ,"ch", sep ='',end='  ' )
                    if i == 3:
                        print("Interference level: ", end='')
                        for j in self.interference_level.keys():
                            if self.interference_level[j] != 0:
                                print("(", j, "ch: ", self.interference_level[j], "Mbps", ")", sep='', end=' ')
                    if i == 4:
                        print("Node info", end='')
                    if i >= 6:
                        for ch in self.channel_list.keys():
                            if (self.channel_list[ch] != []):
                                if ch not in printed_ch:
                                    printed_ch.append(ch)
                                    if (len(self.channel_list[ch]) <= 9):
                                        print(ch ,": ",self.channel_list[ch], sep ='',end='' )
                                        break
                                    else:
                                        print(ch ,": [", end='')
                                        for idx in range(9):
                                            if idx != 8:
                                                print(self.channel_list[ch][idx], ",", end='' )
                                            else:
                                                print(self.channel_list[ch][idx], "...]", end='')
                                        break
                    if i == 10:
                        if self.in_simul == True:
                            print("Current Error:", self.user.error(),"meter", end= '')
                    if i == 11:
                        if self.in_simul == True:
                            print("Average Error:", self.user.whole_error(),"meter", end='')
                    if i == 13:
                        if self.in_simul == True:
                            print("Current Packet loss: ", self.user.packet_loss_each(), "packets",end='')
                    if i == 14:
                        if self.in_simul == True:
                            print("Average Packet loss: ", self.user.avg_packet_loss(), "%", end='')
                    print()
        except:
            print("print grid error")
            input()

    # get command input
    def get_command(self):
        print("      Command: ", end='')
        return input()

    # Command: finish 
    def exit(self,ipt):
        if ipt == "finish":
            print("Bye!")
            return True
        else:
            return False

    # Command: add node 20,20
    def add_node(self,ipt):
        try:
            if "add node" in ipt:
                x_v, y_v = ipt[9:].split(',')
                cor = (int(x_v), int(y_v))
                if self.grid_map.get(cor) == None:
                    print("Incorrect coordinates entered.")
                else:
                    if self.grid_map[cor] == 0:
                        self.grid_map[cor] = nodeset.node(cor, self.ple_seed[11])
                        self.check = True
                        self.node_num += 1
        except:
            print("add node error")
            input()
            return

    # Command: add random 10
    def add_random(self, ipt):
        try:
            if "add random" in ipt:
                node_num = int(ipt[11:])
                for i in range(node_num):
                    cor_x = str(random.randint(1,20))
                    cor_y = str(random.randint(1,20))
                    tmp_ipt = "add node "+ cor_x+","+cor_y
                    self.add_node(tmp_ipt)
        except:
            print("add random error")
            input()
            return


    # Command: remove node 20,20
    def remove_node(self, ipt):
        try:
            if "remove node" in ipt:
                x_v, y_v = ipt[11:].split(',')
                cor = (int(x_v), int(y_v))
                if self.grid_map.get(cor) == None:
                    print("Incorrect coordinates entered.")
                else:
                    if self.grid_map[cor] != 0:
                        self.grid_map[cor] = 0
                        self.check = True
                        self.node_num -= 1
        except:
            print("remove node error")
            input()
            return

    # Command: set channel 20,20 11
    def set_channel(self, ipt):
        try:
            if "set channel" in ipt:
                data = ipt[12:]
                cor_str, channel_num = data.split(' ')
                x_v, y_v = cor_str.split(',')
                cor = (int(x_v), int(y_v))
                if self.grid_map.get(cor) == None:
                    print("Incorrect coordinates entered.")
                else:
                    if self.grid_map[cor] != 0:
                        if int(channel_num) >= 11 or int(channel_num) <= 26:
                            self.grid_map[cor].set_channel(int(channel_num), self.ple_seed[int(channel_num)])
                            self.check = True
                        else:
                            print("Incorrect channel number entered.")
        except:
            print("set channel error")
            input()
            return

    # Command: add user  20,20
    def add_user(self, ipt):
        try:
            if "add user" in ipt:
                x_v, y_v = ipt[9:].split(',')
                cor = []
                cor.append(int(x_v))
                cor.append(int(y_v))
                if self.user_grid.get(tuple(cor)) == None:
                    print("Incorrect coordinates entered.")
                else:
                    if self.user_grid[tuple(cor)] == 0:
                        self.user_grid[tuple(cor)] = 1
                        self.user.set_cov(cor)
                        self.check = True
        except:
            print("add user error")
            input()
            return

    # Command: simul start 20,20
    def simul_start(self, ipt):   
        # try:   
            if "simul start" in ipt:
                x_v, y_v = ipt[11:].split(',')
                self.user.set_goal([int(x_v), int(y_v)])
                self.simulation()
        # except:
        #     print("simul start error")
        #     input()
        #     return

    # Command: set intfer 11 5
    def set_interfer(self, ipt):
        try:
            if "set interfer" in ipt:
                channel_num, intfer = ipt[13:].split(' ')
                channel_num = int(channel_num)
                intfer = int(intfer)
                if intfer != 0 and intfer != 5 and intfer != 10 and intfer != 20 and intfer != 50:
                    print("Incorrect intference entered.")
                else:
                    check = 0
                    for cov_v in self.grid_map.keys():
                        if self.grid_map[cov_v] != 0:
                            node = self.grid_map[cov_v]
                            if node.get_channel() == channel_num:
                                node.set_interfer(intfer)
                                check = 1
                    if check == 1:
                        self.interference_level[channel_num] = intfer
                        self.check = True
        except:
            print("set interfer error")
            input()
            return

    # Wrong command
    def wrong(self):
        print("Wrong command input")
        self.check = False

    # get rssi generation
    def generate_rssi(self):
        rssi_list = []
        for cov_v in self.grid_map.keys():
            if self.grid_map[cov_v] != 0:
                rssi_list.append(self.grid_map[cov_v].beacon(self.user.get_cor()))
        return rssi_list

    # get kalman rssi generation
    def generate_kalman_rssi(self):
        rssi_list = []
        for cov_v in self.grid_map.keys():
            if self.grid_map[cov_v] != 0:
                rssi_list.append(self.grid_map[cov_v].kalman_beacon(self.user.get_cor()))
        return rssi_list

    # Simulation function
    def simulation(self):
        # try:
            self.in_simul = True
            while self.user.get_goal() != self.user.get_cor():
                esti_cor = self.user.estimate(self.generate_rssi())
                # esti_cor = self.user.estimate(self.generate_kalman_rssi())
                self.esti_grid[esti_cor] = 1
                self.clear()
                self.print_grid()
                self.user_grid[tuple(self.user.get_cor())] = 0
                self.user.travel()
                self.user_grid[tuple(self.user.get_cor())] = 1
                self.esti_grid[esti_cor] = 0
            self.simul_print("Simulation Finish!")
            self.check = True
            self.in_simul = False
        # except:
        #     print(self.user.get_goal(), self.user.get_cor())
        #     print("simulation error")
        #     input()
        #     return



