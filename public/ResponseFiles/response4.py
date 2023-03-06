

def complex_function(input_list, input_tuple, input_dict):
    """
    This function takes 3 input arguments and returns a list of tuples
    with the elements of the list, tuple, and dict.
    """
    result = []
    for item in input_list:
        for key, value in input_dict.items():
            if item == key:
                result.append((item, value))
    for item in input_tuple:
        for key, value in input_dict.items():
            if item == key:
                result.append((item, value))
    return result