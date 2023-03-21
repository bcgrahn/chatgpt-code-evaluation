
def check_duplicate_letters(sentence):
    """
    Check for duplicate letters in a sentence.

    Parameters
    ----------
    sentence : str
        Sentence to be checked.

    Returns
    -------
    bool
        True if sentence has any word with duplicate letters, else False.
    """
    words = sentence.split()
    for word in words:
        if len(word) != len(set(word)):
            return True
    return False