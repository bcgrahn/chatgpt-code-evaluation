

def capital_indexes(string):
    """
    Returns a list of all the indexes in the string that have capital letters.

    Parameters:
        string (str): A string.

    Returns:
        list: A list of all the indexes in the string that have capital letters.
    """
    capital_indexes_list = []
    for i in range(len(string)):
        if string[i].isupper():
            capital_indexes_list.append(i)
    return capital_indexes_list