import socket
import common_ports
import re

def get_open_ports(target, port_range, verbose = False):
    open_ports = []
    time = 10
    isIP = re.search(r'\d', target)

    if verbose:
        ip_address = socket.gethostbyname(target)
        open_ports = f'Open ports for {target}{ '' if isIP else f' ({ip_address})' }\nPORT     SERVICE'; 
        for port in range(port_range[0],port_range[1]+1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(time)
            spaceQuantity = 6
            try:
                if port != 443: #TODO remove, just a workaround
                    s.connect((target, port))
                    spaceQuantity = 7
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
                if isIP:
                    open_ports = 'Error: Invalid IP address'
                else:
                    open_ports = 'Error: Invalid hostname'
                break
            except socket.error as e:
                print(f'ERROR:\ttarget: {target}\t\tport: {port}\terror: {e}')
            finally:
                s.close()

    return(open_ports)