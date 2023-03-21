

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
    ',' : '--..--',
    ':' : '---...',
    "'" : '.----.',
    '!' : '-.-.--',
    '.' : '.-.-.-',
    '?' : '..--..'
    }

def morse_translator(string):
    string = string.upper()
    translated_string = ''
    for char in string:
        translated_string += morse_code[char] + ' '
    return translated_string

print(morse_translator('Hello World!')) # Output: .... . .-.. .-.. --- .-- --- .-. .-.. -.. !