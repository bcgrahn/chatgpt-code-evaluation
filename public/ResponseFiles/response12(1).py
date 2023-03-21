

def parse_string(encoded_string):
  # Split the string by any number of zeros
  split_string = encoded_string.split('0')
  
  # Get the first name
  first_name = split_string[0]
  
  # Get the last name
  last_name = split_string[1]
  
  # Get the id
  id = split_string[-1]
  
  # Create a dictionary
  parsed_dict = {
    "first_name": first_name,
    "last_name": last_name,
    "id": id
  }
  
  # Return the dictionary
  return parsed_dict

print(parse_string("John000Doe000123"))