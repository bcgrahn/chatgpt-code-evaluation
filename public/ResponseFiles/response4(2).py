

def is_palindrome(s):
    """
    Checks if a given string is a palindrome.
    
    Parameters
    ----------
    s : str
        String to check if it is a palindrome.
    
    Returns
    -------
    bool
        True if the given string is a palindrome, else False.
    """
    return s == s[::-1]