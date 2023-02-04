from unidecode import unidecode

char_to_dots = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
    ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
    '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

""""
    Function to encode morse code. Recive a str and return encoded in morse
"""


def encodeMorse(stringToEncode):
    stringToEncode = processingStr(stringToEncode)
    morseCode = ""
    for char in stringToEncode:
        if(char in char_to_dots):
            morseCode += char_to_dots[char]+" "
    return processingStr(morseCode[:-1])


""""
    Function to process a morse code and return a string text
"""


def decodeMorse(stringToDecode):
    stringToDecode = processingStr(stringToDecode)
    stringToDecode = stringToDecode.split()
    stringFinal = ""
    for letter in stringToDecode:
        for key in char_to_dots.keys():
            if(char_to_dots[key] == letter):
                stringFinal += key + " "
    return processingStr(stringFinal[:-1])


""" 
    Processing a str, remove unnecessary spaces into string and 
    transform a str in uppercase, replace strings using unidecode
"""


def processingStr(string):
    newStr = ""
    for i in range(len(string)):
        if(string[i] == " " and string[i-1] == " "):
            pass
        else:
            newStr += string[i]
    return unidecode(newStr.upper())
