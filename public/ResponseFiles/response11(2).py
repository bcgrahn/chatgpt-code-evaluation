

import socket

def get_domain_name(ip_address):
    """
    Function to find the domain name from an IP address using PTR records.
    
    Parameters:
    ip_address (str): The IP address to look up.
    
    Returns:
    str: The domain name associated with the IP address.
    """
    try:
        return socket.gethostbyaddr(ip_address)[0]
    except socket.herror:
        return None