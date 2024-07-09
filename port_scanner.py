import socket
import common_ports
import re

def get_open_ports(target, port_range, verbose = False):
    open_ports = []

    if verbose: # TODO
        ip_address = '192.168.0.10'
        open_ports = f'Open ports for {target} ({ip_address})\nPORT\tSERVICE\n'; 
    else: 
        for port in range(port_range[0],port_range[1]+1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(30)
            try:
                s.connect((target, port))
                open_ports.append(port)
            except socket.gaierror as e:
                print(e)
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

# ports = get_open_ports("scanme.nmap", [22, 42], False)
# ports = get_open_ports("266.255.9.10", [22, 42], False)
ports = get_open_ports('209.216.230.240', [440, 445])
# ports = get_open_ports('www.stackoverflow.com', [79, 82])
print("Open ports:", ports, "\n")