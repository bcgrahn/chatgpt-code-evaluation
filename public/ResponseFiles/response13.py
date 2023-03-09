

import socket 

def find_domain_name(ip_address):
    domain_name = socket.gethostbyaddr(ip_address)
    return domain_name[0]