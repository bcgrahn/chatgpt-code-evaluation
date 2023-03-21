

def dec_to_hex(string):
    """Convert a string of ASCII characters to hexadecimal.

    Parameters:
    string (str): A string of ASCII characters.

    Returns:
    hex_string (str): A string of hexadecimal values separated by spaces.
    """
    hex_string = ""
    for char in string:
        hex_string += hex(ord(char))[2:].zfill(2) + " "
    return hex_string.lower()