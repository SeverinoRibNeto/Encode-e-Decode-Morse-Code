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
"""
 Passos para codificar string em morse
 Passo 1: Receber string;
 Passo 2: Tratar string;
 Passo 3: Começar a montar a nova string com o morse;
 Passo 4: Retornar a string alterada;
"""


def encodeMorse(stringToEncode):
    stringToEncode = processingStr(stringToEncode)

    return


""" Processing a str, remove unnecessary spaces into string and 
    transform a str in uppercase
"""


def processingStr(string):
    newStr = ""
    for i in range(len(string)):
        if(string[i] == " " and string[i-1] == " "):
            pass
        else:
            newStr += string[i]
    return newStr.upper()
