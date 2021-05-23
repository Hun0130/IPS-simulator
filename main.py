import node as nodeset
import rssi
import user
import systems 

def main():
    sys = systems.system()
    while (True):
        sys.clear()
        sys.update()
        sys.print_grid()
        input = sys.get_command()
        if "test1" in input: test1()
        if "re" in input: sys = systems.system()
        if input == "": continue
        if sys.exit(input):
            break
        sys.add_node(input)
        sys.add_random(input)
        sys.remove_node(input)
        sys.set_channel(input)
        sys.set_interfer(input)
        sys.add_user(input)
        sys.simul_start(input)
    return

def test1():
    sys = systems.system()
    sys.add_node("add node 1,1")
    sys.add_node("add node 1,5")
    sys.add_node("add node 5,1")
    sys.add_node("add node 1,20")
    sys.add_node("add node 5,20")
    sys.add_node("add node 1,15")
    sys.add_node("add node 20,1")
    sys.add_node("add node 15,1")
    sys.add_node("add node 20,5")
    sys.add_node("add node 20,20")
    sys.add_node("add node 15,20")
    sys.add_node("add node 20,15")
    sys.add_node("add node 5,5")
    sys.add_node("add node 5,15")
    sys.add_node("add node 15,5")
    sys.add_node("add node 15,15")
    sys.add_node("add node 10,1")
    sys.add_node("add node 1,10")
    sys.add_node("add node 10,5")
    sys.add_node("add node 5,10")
    sys.add_node("add node 20,10")
    sys.add_node("add node 10 20")
    sys.add_node("add node 10,10")
    sys.add_node("add node 15,10")
    sys.add_node("add node 10,15")
    sys.add_node("add node 10,20")
    sys.set_interfer("set interfer 11 50")
    sys.add_user("add user 1,1")
    sys.update()
    sys.simul_start("simul start 20,20")
    return sys.user.whole_error()

def test2():
    sys = systems.system()
    sys.add_random("add random 10")
    sys.add_user("add user 1,1")
    sys.update()
    sys.simul_start("simul start 20,20")
    # sys.set_interfer("set interfer 11 20")
    return sys.user.whole_error()

def test_log():
    log = 0
    log_num = 0
    for i in range(100):
        log += test1()
        log_num += 1
    return log / log_num

if __name__ == '__main__':
    print(test_log())
    # main()
    