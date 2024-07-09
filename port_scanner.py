import socket
import common_ports
import re

def get_open_ports(target, port_range, verbose = False):
    open_ports = []
    time = 10

    if verbose:
        ip_address = socket.gethostbyname(target)
        open_ports = f'Open ports for {target} ({ip_address})\nPORT     SERVICE'; 
        for port in range(port_range[0],port_range[1]+1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(time)
            spaceQuantity = 7
            try:
                if port != 443: #TODO remove, just a workaround
                    s.connect((target, port))
                    spaceQuantity = 6 
                open_ports += f'\n{port}{' ' * spaceQuantity }{common_ports.ports_and_services[port]}'
            except socket.error as e:
                print(f'ERROR:\ttarget: {target}\t\tport: {port}\terror: {e}')
            finally:
                s.close()
    else: 
        for port in range(port_range[0],port_range[1]+1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(time)
            try:
                if port != 443: #TODO remove, just a workaround
                    s.connect((target, port))
                open_ports.append(port)
            except socket.gaierror as e:
                if re.search(r'\d', target):
                    open_ports = 'Error: Invalid IP address'
                else:
                    open_ports = 'Error: Invalid hostname'
                break
            except socket.error as e:
                print(f'ERROR:\ttarget: {target}\t\tport: {port}\terror: {e}')
            finally:
                s.close()

    return(open_ports)

# calls bellow just for test
# ports = get_open_ports("scanme.nmap", [22, 42], False)
# ports = get_open_ports("266.255.9.10", [22, 42], False)
# ports = get_open_ports("scanme.nmap.org", [20, 80], True)
# ports = get_open_ports("137.74.187.104", [440, 450], True)
# ports = get_open_ports('209.216.230.240', [440, 445])
# ports = get_open_ports('www.stackoverflow.com', [79, 82])
# print("Open ports:", ports, "\n")