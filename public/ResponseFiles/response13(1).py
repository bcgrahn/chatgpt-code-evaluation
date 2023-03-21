

def dec_to_hex(string):
  # Initialize empty string
  hex_string = ""
  
  # Iterate through each character in the string
  for char in string:
    # Get the decimal representation of the character
    dec_val = ord(char)
    
    # Convert the decimal value to hexadecimal
    hex_val = hex(dec_val)[2:]
    
    # Append the hexadecimal value to the hex string
    hex_string += hex_val + " "
  
  # Return the hex string with all lowercase characters
  return hex_string.lower()