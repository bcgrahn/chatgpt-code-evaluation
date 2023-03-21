
def palindrome(string):
    """
    Check if the string is a palindrome
    :param string: the string to check
    :return: True if the string is a palindrome, False otherwise
    """
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    return False

