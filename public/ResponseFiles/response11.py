

# Create a dictionary to store the Morse code
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-', ' ':' '} 

# Function to encrypt the string according to the Morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            # Looks up the dictionary and adds the correspponding value
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters and 2 indicates different words
            cipher += ' '
    return cipher

# Function to decrypt the string according to the Morse code chart
def decrypt(message):
    # extra space added at the end to access the last Morse code
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        # checks for space
        if (letter != ' '):
            # counter to keep track of space
            i = 0
            citext += letter
        # if i = 1 that indicates a new character
        elif i == 1:
            # adding space to separate words
            decipher += ' '
        else:
            # accessing the keys using their values (reverse of encryption)
            decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
            citext = ''
        i += 1
    return decipher

# Driver code
if __name__ == '__main__':
    message = input("Enter a message: ")
    result = encrypt(message.upper())
    print (result)
    result = decrypt(result)
    print (result)