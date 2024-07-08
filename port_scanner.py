import socket

def get_open_ports(target, port_range, verbose = False):
    open_ports = []

    if verbose:
        ip_address = '192.168.0.10'
        open_ports = f'Open ports for {target} ({ip_address})\nPORT\tSERVICE\n'; 
        
    else: 
        open_ports.append(1)

    return(open_ports)

ports = get_open_ports("www.freecodecamp.org", [75, 85], True)
print("Open ports:", ports, "\n")