

def parse_string(encoded_string):
  #Split the string by zeros
  split_string = encoded_string.split("0")

  #Get the first name and last name
  first_name = split_string[0]
  last_name = split_string[1]

  #Get the id
  id = split_string[2]

  #Create a dictionary with the values
  parsed_string = {
    "first_name": first_name,
    "last_name": last_name,
    "id": id
  }

  #Return the dictionary
  return parsed_string