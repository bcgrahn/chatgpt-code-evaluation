
def parse_string(encoded_str):
    """Parses an encoded string and returns a dictionary with the first name, last name, and id values."""
    # Split string by zeros
    split_str = encoded_str.split('0')
    
    # Create dictionary
    response = {
        "first_name": split_str[0],
        "last_name": split_str[1],
        "id": split_str[2]
    }
    
    return response