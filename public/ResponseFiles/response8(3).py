
def check_duplicate_letter(sentence):
    """
    Function to check if a sentence has any word with duplicate letters

    Parameters:
    sentence (str): Sentence to check for duplicate letters

    Returns:
    bool: True if the sentence has any word with duplicate letters, else False
    """
    words = sentence.split()
    for word in words:
        for i, letter in enumerate(word):
            if word.count(letter) > 1:
                return True
    return False