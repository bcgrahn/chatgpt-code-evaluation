
def decimal_to_hex(decimal_string):
    """
    Converts a decimal string to a hexadecimal string.
    
    Parameters
    ----------
    decimal_string : str
        A string of ASCII characters.
        
    Returns
    -------
    hex_string : str
        A string of hexadecimal characters.
    """
    hex_string = ''
    for char in decimal_string:
        hex_string += format(ord(char), 'x').lower() + ' '
    return hex_string.strip()