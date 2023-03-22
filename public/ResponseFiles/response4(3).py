
def is_palindrome(s):
    """
    Return True if the given string is a palindrome, else return False.

    Parameters:
    s (str): The string to check.

    Returns:
    bool: True if the given string is a palindrome, else False.
    """
    return s == s[::-1]
