import node as nodeset
import rssi
import user
import systems

def main():
    system = systems.system
    while (True):
        system.clear()
        system.update()
        system.print_grid()
        input = system.get_command()
        system.add_node(input)
        system.remove_node(input)
        system.set_channel(input)
        system.set_interfer(input)
        system.add_user(input)
        system.simul_set(input)
        if system.exit(input):
            return

if __name__ == '__main__':
    main()