

import socket 

def find_domain_name(ip_address):
    return socket.gethostbyaddr(ip_address)[0]