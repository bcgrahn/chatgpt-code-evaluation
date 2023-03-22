

def dec_to_hex(string):
    hex_string = ""
    for char in string:
        hex_string += hex(ord(char))[2:].zfill(2) + " "
    return hex_string.lower()