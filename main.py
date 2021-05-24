import systems 
import test

def main():
    sys = systems.system()
    while (True):
        sys.clear()
        sys.update()
        sys.print_grid()
        input = sys.get_command()
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


if __name__ == '__main__':
    #main()
    test.test_log()