

def decimal_to_hex(string):
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate through each character in the string
    for char in string:
        # Convert the character to its decimal equivalent
        decimal = ord(char)
        
        # Convert the decimal to its hexadecimal equivalent
        hexadecimal = hex(decimal)
        
        # Append the hexadecimal value to the result string
        result += hexadecimal[2:] + ' '
        
    # Return the result string
    return result.lower()