

def complex_code(input_list):
    """
    This function takes an input list and performs a complex operation on it.
    """
    output_list = []

    for item in input_list:
        if isinstance(item, int):
            output_list.append(item * 2)
        elif isinstance(item, str):
            output_list.append(item[::-1])
        else:
            output_list.append(item)

    return output_list