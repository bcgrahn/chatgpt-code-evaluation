
def palindrome(string):
    """
    Checks if a string is a palindrome.

    Args:
        string (str): The string to be checked.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """

    return string == string[::-1]

