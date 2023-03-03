

def add_two_numbers(x, y):
    """
    Function to add two numbers
    """
    try:
        return x + y
    except TypeError:
        raise TypeError("Inputs must be numeric")