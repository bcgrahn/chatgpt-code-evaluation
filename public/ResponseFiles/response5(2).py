

def capital_indexes(string):
    """
    Returns a list of all the indexes in the string that have capital letters
    """
    capital_index_list = []
    for index, letter in enumerate(string):
        if letter.isupper():
            capital_index_list.append(index)
    return capital_index_list