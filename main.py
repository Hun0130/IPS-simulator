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
    sys.add_random("add random 12")
    sys.add_user("add user 1,1")
    sys.simul_start("simul start 20,20")
    
if __name__ == '__main__':
    main()