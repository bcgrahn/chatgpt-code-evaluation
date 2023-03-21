
import string

def morse_code_translator(input_string):
    """
    Function to translate a string to Morse code.
    """
    morse_code = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        ',': '--..--',
        '.': '.-.-.-',
        '?': '..--..',
        "'": '.----.',
        '!': '-.-.--',
        '/': '-..-.',
        '(': '-.--.',
        ')': '-.--.-',
        '&': '.-...',
        ':': '---...',
        ';': '-.-.-.',
        '=': '-...-',
        '+': '.-.-.',
        '-': '-....-',
        '_': '..--.-',
        '"': '.-..-.',
        '$': '...-..-',
        '@': '.--.-.'
    }

    output_string = ''

    for character in input_string.upper():
        if character in string.ascii_uppercase:
            output_string += morse_code[character] + ' '
        elif character in string.digits:
            output_string += morse_code[character] + ' '
        elif character in morse_code:
            output_string += morse_code[character] + ' '
        else:
            output_string += character

    return output_string.strip()

# Test code
print(morse_code_translator("Hello World"))
print(morse_code_translator("SOS"))
print(morse_code_translator("I love Python!"))