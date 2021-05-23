import os
from typing import ChainMap
import node as nodeset
import user as us
import random

class system:
    # use for check to update graphic
    check = True
    
    # number of sensor nodes
    node_num = 0
    
    # user node
    user =  us.user((0, 0))
    
    # the list of the channel used now
    channel_list = {}
    for i in range(11, 27):
        channel_list[i] = []
    
    # the level of Interference
    interference_level = {}
    for i in range(11, 27):
        interference_level[i] = 0
    
    # grid_map information
    grid_map = {}
    for i in range(1, 21):
        for j in range(1, 21):
            grid_map[(i,j)] = 0
    
    # user grid information
    user_grid = {}
    for i in range(1, 21):
        for j in range(1, 21):
            user_grid[(i,j)]= 0
    
    # estimation grid information
    esti_grid = {}
    for i in range(1, 21):
        for j in range(1, 21):
            esti_grid[(i,j)] = 0

    def update():
        for i in range(11, 27):
            system.channel_list[i] = []
        for cov_v in system.grid_map.keys():
            if system.grid_map[cov_v] != 0:
                node = system.grid_map[cov_v]
                if node.get_cor() not in system.channel_list[node.get_channel()]:
                    system.channel_list[node.get_channel()].append(node.get_cor())
        return

    # erase consol graphic
    def clear():
        if system.check == True:
            os.system('clear')

    # Center Alignment Output
    def simul_print(string):
        print("{:^100}".format(string))

    # print grid
    def print_grid():
        if system.check == True:
            system.simul_print("Indoor Localization Simulator")
            system.simul_print(" 1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20 ")
            system.simul_print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
            for i in range(1, 21):
                grid__input = str(i) + " |"
                for key in system.grid_map.keys():
                    if key[0] == i:
                        if system.grid_map[key] != 0:
                            grid__input += "S"
                        if not system.grid_map[key] != 0:
                            grid__input += " "
                        if system.user_grid[key] != 0:
                            grid__input += "R"
                        if not system.user_grid[key] != 0:
                            grid__input += " "
                        if system.esti_grid[key] != 0:
                            grid__input += "E"
                        if not system.esti_grid[key] != 0:
                            grid__input += " "
                        grid__input += "|"
                if i < 10:
                    grid__input += "  "
                else:
                    grid__input += "   "
                system.simul_print(grid__input)
                print("         |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|", end='  ') 
                if i == 1:
                    print("Sensor node: ", system.node_num, end='')
                if i == 2:
                    print("Channel State: ", end = '')
                    for ch in system.channel_list.keys():
                        if (system.channel_list[ch] != []):
                            print(len(system.channel_list[ch])," nodes in ",ch ,"ch", sep ='',end='  ' )
                if i == 3:
                    print("Interference level: ", end='')
                    for i in system.interference_level.keys():
                        if system.interference_level[i] != 0:
                            print("(", i, "ch: ", system.interference_level[i], "Mbps", ")", sep='', end=' ')
                if i == 4:
                    print("Node info", end='')
                line_num = 5
                for ch in system.channel_list.keys():
                    if (system.channel_list[ch] != []):
                        if i == line_num:
                            if (len(system.channel_list[ch]) <= 10):
                                print(ch ,": ",system.channel_list[ch], sep ='',end='  ' )
                            else:
                                print(ch ,": [", end='')
                                for idx in range(10):
                                    if idx != 9:
                                        print(system.channel_list[ch][idx], ",", end='' )
                                    else:
                                        print(system.channel_list[ch][idx], "...]", end='')
                            line_num += 1
                else:
                    print()

    # get command input
    def get_command():
        print("Command: ", end='')
        return input()

    # Command: finish 
    def exit(ipt):
        if ipt == "finish":
            print("Bye!")
            return True
        else:
            return False

    # Command: add node 20,20
    def add_node(ipt):
        try:
            if "add node" in ipt:
                x_v, y_v = ipt[9:].split(',')
                cor = (int(x_v), int(y_v))
                if system.grid_map.get(cor) == None:
                    print("Incorrect coordinates entered.")
                else:
                    if system.grid_map[cor] == 0:
                        system.grid_map[cor] = nodeset.node(cor)
                        system.check = True
                        system.node_num += 1
        except:
            system.wrong()

    # Command: add random 10
    def add_random(ipt):
        try:
            if "add random" in ipt:
                node_num = int(ipt[11:])
                for i in range(node_num):
                    cor_x = str(random.randint(1,20))
                    cor_y = str(random.randint(1,20))
                    tmp_ipt = "add node "+ cor_x+","+cor_y
                    system.add_node(tmp_ipt)
        except:
            return


    # Command: remove node 20,20
    def remove_node(ipt):
        try:
            if "remove node" in ipt:
                x_v, y_v = ipt[11:].split(',')
                cor = (int(x_v), int(y_v))
                if system.grid_map.get(cor) == None:
                    print("Incorrect coordinates entered.")
                else:
                    if system.grid_map[cor] != 0:
                        system.grid_map[cor] = 0
                        system.check = True
                        system.node_num -= 1
        except:
            return

    # Command: set channel 20,20 11
    def set_channel(ipt):
        try:
            if "set channel" in ipt:
                data = ipt[12:]
                cor_str, channel_num = data.split(' ')
                x_v, y_v = cor_str.split(',')
                cor = (int(x_v), int(y_v))
                if system.grid_map.get(cor) == None:
                    print("Incorrect coordinates entered.")
                else:
                    if system.grid_map[cor] != 0:
                        if int(channel_num) >= 11 or int(channel_num) <= 26:
                            system.grid_map[cor].set_channel(int(channel_num))
                            system.check = True
                        else:
                            print("Incorrect channel number entered.")
        except:
            system.wrong()

    # Command: add user  20,20
    def add_user(ipt):
        try:
            if "add user" in ipt:
                x_v, y_v = ipt[9:].split(',')
                cor = []
                cor.append(int(x_v))
                cor.append(int(y_v))
                if system.user_grid.get(tuple(cor)) == None:
                    print("Incorrect coordinates entered.")
                else:
                    if system.user_grid[tuple(cor)] == 0:
                        system.user_grid[tuple(cor)] = 1
                        system.user.set_cov(cor)
                        system.check = True
        except:
            return

    # Command: simul set
    def simul_set(ipt):      
        try:
            if ipt in "simul set":
                print("Goal to go: ", end='')
                goal = input()
                x_v, y_v = goal.split(',')
                system.user.set_goal([int(x_v), int(y_v)])
                print("Do you want to start simulation? (Y/N): ", end='')
                yn = input()
                if (str(yn) in "Y") or (str(yn) in "y"):
                    system.simulation()
                    return
                else:
                    return
        except:
            return

    # Command: set intfer 11 5
    def set_interfer(ipt):
        try:
            if "set interfer" in ipt:
                channel_num, intfer = ipt[13:].split(' ')
                channel_num = int(channel_num)
                intfer = int(intfer)
                if intfer != 0 and intfer != 5 and intfer != 10 and intfer != 20:
                    print("Incorrect intference entered.")
                else:
                    check = 0
                    for cov_v in system.grid_map.keys():
                        if system.grid_map[cov_v] != 0:
                            node = system.grid_map[cov_v]
                            if node.get_channel() == channel_num:
                                node.set_interfer(intfer)
                                check = 1
                    if check == 1:
                        system.interference_level[channel_num] = intfer
                        system.check = True
        except:
            return

    # Wrong command
    def wrong():
        print("Wrong command input")
        system.check = False

    # get rssi generation
    def generate_rssi():
        rssi_list = []
        for cov_v in system.grid_map.keys():
            if system.grid_map[cov_v] != 0:
                rssi_list.append(system.grid_map[cov_v].beacon(system.user.get_cor()))
        return rssi_list

    # Simulation function
    def simulation():
        try:
            while system.user.get_goal() != system.user.get_cor():
                esti_cor = system.user.estimate(system.generate_rssi())
                system.user_grid[tuple(system.user.get_cor())] = 0
                system.user.travel()
                system.user_grid[tuple(system.user.get_cor())] = 1
                system.esti_grid[esti_cor] = 1
                input()
                system.clear()
                system.print_grid()
                system.esti_grid[esti_cor] = 0
            system.check = True
        except:
            return



