

def decimal_to_hex(string):
    """Convert a string of ASCII characters to a hexadecimal string.

    Args:
        string (str): A string of ASCII characters.

    Returns:
        str: A string of hexadecimal characters separated by spaces.
    """
    hex_string = ""
    for char in string:
        hex_string += hex(ord(char))[2:].zfill(2) + " "
    return hex_string.lower()