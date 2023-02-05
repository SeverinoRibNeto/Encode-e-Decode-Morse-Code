import os
import time
from tkinter import *
from tkinter import ttk

from playsound import playsound

import encodeMorse

"""
        Functions to help interface
    """


###GLOBAL VAR####
textEntry = ''
lang = 'English'  # Initial language
radioSelect = ''  # Option Radio Button

###LANG DICT###
langPtBr = {"language": "Português Brasil",
            "titleWindow": "",
            "projectTitle": "Codificador e Decodificador de Código Morse",
            "instru": "Use esse aplicativo para gerar um código Morse, decodificar e escutar esse código",
            "infoText": "Escreva a mensagem a ser códificada em código Morse",
            "textBtnCode": "Codificar Mens",
            "textBtnDecode": "Decodificar Mens",
            "titleFrame2": "Mensagem em Código Morse",
            "playsoundsBtn": "Tocar Código Morse",
            "radioCode": "Codificar",
            "radioDecode": "Decodificar"}

langEn = {"language": "English",
          "titleWindow": "",
          "projectTitle": "Encode and Decode Morse Code",
          "instru": "Use this app to generate a Morse code, decode and listen a sound of code",
          "infoText": "Write your message to code to Morse code:",
          "textBtnCode": "Encode Message",
          "textBtnDecode": "Decode Message",
          "titleFrame2": "Message in Morse Code",
          "playsoundsBtn": "Play Morse Code",
          "radioCode": "Code",
          "radioDecode": "Decode"}
# END LANG VAR

# Function to play sounds from a string.


def playSounds(sounds):
    for som in sounds:
        if (som == ' '):
            time.sleep(0.4)
        elif(som not in sounds):
            print("Error! Sound not in list of sounds")
        else:
            playsound(
                os.path.join(os.getcwd(), 'sounds', som + '.wav'))

# Function to encoding morse and show in Text Widget


def encodingMorse():
    global textEntry
    morseCodeTxBox.delete('1.0', 'end')
    textEntry = textToConvertEn.get()
    codeMorse = encodeMorse.encodeMorse(textEntry)
    morseCode.set(codeMorse)
    morseCodeTxBox.insert(END, codeMorse)

# Function to decoding morse and show in Text Widget


def decodingMorse():
    global textEntry
    morseCodeTxBox.delete('1.0', 'end')
    textEntry = textToConvertEn.get()
    codeMorse = encodeMorse.decodeMorse(textEntry)
    morseCode.set(codeMorse)
    morseCodeTxBox.insert(END, codeMorse)


def decodingMorseToSong():
    decode = encodeMorse.decodeMorse(morseCode.get())
    playSounds(decode)


# Function to modify a button text lang and selection 'code' or 'decode' using radio button
def radioSelection():
    global lang, langEn, langPtBr, radioSelect
    radioSelect = str(optionVar.get())
    if(str(optionVar.get()) == 'decode' and lang == langEn["language"]):
        txtBtn.set(langEn["textBtnDecode"])
        encodeBtn['textvariable'] = txtBtn
        encodeBtn['command'] = decodingMorse
    elif(str(optionVar.get()) == 'decode' and lang == langPtBr["language"]):
        txtBtn.set(langPtBr["textBtnDecode"])
        encodeBtn['textvariable'] = txtBtn
        encodeBtn['command'] = decodingMorse
    elif(str(optionVar.get()) == 'code' and lang == langEn["language"]):
        txtBtn.set(langEn["textBtnCode"])
        encodeBtn['textvariable'] = txtBtn
        encodeBtn['command'] = encodingMorse
    elif(str(optionVar.get()) == 'code' and lang == langPtBr["language"]):
        txtBtn.set(langPtBr["textBtnCode"])
        encodeBtn['textvariable'] = txtBtn
        encodeBtn['command'] = encodingMorse
    else:
        print("Error!")

# Function to modify language using option menu. Two language selected: Portuguese and English


def changeLanguage(choise):
    global lang, langPtBr, langEn, radioSelect
    lang = choise
    if(choise == langPtBr["language"]):
        projectTitleTxt.set(langPtBr["projectTitle"])
        instruTxt.set(langPtBr["instru"])
        infoTextTxt.set(langPtBr["infoText"])
        radioCode.set(langPtBr["radioCode"])
        radioDecode.set(langPtBr["radioDecode"])
        if(radioSelect == 'decode'):
            txtBtn.set(langPtBr["textBtnDecode"])
        elif(radioSelect == 'code'):
            txtBtn.set(langPtBr["textBtnCode"])
        titleFrame2Txt.set(langPtBr["titleFrame2"])
        playsoundsBtn['textvariable'] = playsoundsBtnTxt.set(
            langPtBr["playsoundsBtn"])

    elif(choise == langEn["language"]):
        projectTitleTxt.set(langEn["projectTitle"])
        instruTxt.set(langEn["instru"])
        infoTextTxt.set(langEn["infoText"])
        radioCode.set(langEn["radioCode"])
        radioDecode.set(langEn["radioDecode"])
        if(radioSelect == 'decode'):
            txtBtn.set(langEn["textBtnDecode"])
        elif(radioSelect == 'code'):
            txtBtn.set(langEn["textBtnCode"])
        titleFrame2Txt.set(langEn["titleFrame2"])
        playsoundsBtnTxt.set(langEn["playsoundsBtn"])

    else:
        pass


"""
    Inicial screen variables
"""


inicialScreen = Tk()
inicialScreen.title("Encode and Decode Morse Code")

frame = ttk.Frame(inicialScreen, padding=20)
frame.grid()
frame2 = ttk.Frame(inicialScreen, padding=20)
frame2.grid()

# Text Var Declaration
projectTitleTxt = StringVar(None, "Encode and Decode Morse Code")
instruTxt = StringVar(
    None, "Use this app to generate a Morse code, decode and listen a sound of code")
infoTextTxt = StringVar(None, "Write your message to code to Morse code:")
radioCode = StringVar(None, "Code")
radioDecode = StringVar(None, "Decode")
txtBtn = StringVar(None, "Encode Message")
titleFrame2Txt = StringVar(None, "Message in Morse Code")
playsoundsBtnTxt = StringVar(None, "Play Morse Code")

"""
        First frame components
"""
titleProjLb = Label(frame,
                    textvariable=projectTitleTxt,
                    font=('Arial Bold', 20)
                    )
titleProjLb.grid(columns=3, row=0)

# language components
langList = [langPtBr["language"], langEn["language"]]
langSelected = StringVar(inicialScreen, "Language")
langSelect = OptionMenu(frame, langSelected, *langList, command=changeLanguage)
langSelect.grid(columns=1, row=0, padx=10, pady=10)
# Instruction components
instrucLb = Label(frame, textvariable=instruTxt,
                  font=('Arial normal', 12))
instrucLb.grid(columns=2, row=1, padx=10, pady=10)

infoTextLb = Label(frame, textvariable=infoTextTxt)
infoTextLb.grid(columns=1, row=2, padx=10, pady=10)
# convertion components
textToConvertEn = Entry(frame, width=100)
textToConvertEn.grid(column=1, row=2, padx=20, pady=20)

# Radio component to select operation 'code' to code in Morse or 'decode' to chose decode in Morse
optionVar = StringVar(None, 'code')
Radiobutton(frame, value='code', variable=optionVar, textvariable=radioCode, command=radioSelection).grid(
    column=0, row=3, padx=10, pady=10)
Radiobutton(frame, value='decode', variable=optionVar, textvariable=radioDecode, command=radioSelection).grid(
    column=1, row=3, padx=10, pady=10)

# button to execute a code or decode
encodeBtn = Button(frame, textvariable=txtBtn, command=encodingMorse)
encodeBtn.grid(column=2, row=3, padx=10, pady=10)


"""
    Second frame components
"""
titleFrame2 = Label(frame2, textvariable=titleFrame2Txt)
titleFrame2.grid(column=1, row=4, padx=10, pady=10)
# Part to show results of code or decode code.
morseCode = StringVar()
morseCodeTxBox = Text(frame2, height=5, width=100,
                      bg="light cyan")
morseCodeTxBox.grid(column=1, row=6, padx=20, pady=20)

# This button play sound. Its work only code option
playsoundsBtn = Button(frame2, textvariable=playsoundsBtnTxt,
                       command=decodingMorseToSong)
playsoundsBtn.grid(column=2, row=6)

# Create a screen
inicialScreen.mainloop()
