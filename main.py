import os
import time
from functools import partial
from tkinter import *
from tkinter import ttk

from playsound import playsound

import encodeMorse

"""
        Functions to help interface
    """


###GLOBAL VAR####
textEntry = ''


def playSounds(sounds):
    for som in sounds:
        if (som == ' '):
            time.sleep(0.4)
        elif(som not in sounds):
            print("Error! Sound not in list of sounds")
        else:
            playsound(
                os.path.join(os.getcwd(), 'sounds', som + '.wav'))


def encodingMorse():
    global textEntry
    print(textEntry)
    textEntry = textToConvertEn.get()
    codeMorse = encodeMorse.encodeMorse(textEntry)
    morseCode.set(codeMorse)


def decodingMorseToSong():
    decode = encodeMorse.decodeMorse(morseCode.get())
    playSounds(decode)


"""
    Inicial screen variables
"""


inicialScreen = Tk()
inicialScreen.title("Encode and Decode Morse Code")

frame = ttk.Frame(inicialScreen, padding=20)
frame.grid()
frame2 = ttk.Frame(inicialScreen, padding=20)
frame2.grid()

"""
        First frame components
"""
titleProjLb = Label(frame,
                    text="Encode and Decode Morse Code",
                    font=('Arial Bold', 20)
                    )
titleProjLb.grid(columns=2, row=0)

instrucLb = Label(frame, text="Use this app to generate a Morse code, decode and listen a sound of code",
                  font=('Arial normal', 12))
instrucLb.grid(columns=2, row=1, padx=10, pady=10)

infoTextLb = Label(frame, text="Write your message to code to Morse code:")
infoTextLb.grid(columns=1, row=2, padx=10, pady=10)

textToConvertEn = Entry(frame, width=100)
textToConvertEn.grid(column=1, row=2, padx=20, pady=20)

encodeBnt = Button(frame, text="Encode Message",
                   command=encodingMorse)
encodeBnt.grid(column=1, row=3, padx=10, pady=10)


"""
    Second frame components
"""
titleFrame2 = Label(frame2, text="Message in Morse Code")
titleFrame2.grid(column=1, row=4, padx=10, pady=10)
morseCode = StringVar()
morseTextLb = Label(frame2, textvariable=morseCode, bg="white")
morseTextLb.grid(column=1, row=5, padx=20, pady=20)

"""
        Comando de tocar quase completo. Precisa ajustar.
    """
playsoundsBnt = Button(frame2, text="Play Morse Code",
                       command=decodingMorseToSong)
playsoundsBnt.grid(column=2, row=6)
inicialScreen.mainloop()
