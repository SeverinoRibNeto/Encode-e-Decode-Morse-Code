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

###LANG DICT###
langPtBr = {"language": "Português Brasil",
            "titleWindow": "",
            "projectTitle": "Codificador e Decodificador de Código Morse",
            "instru": "Use esse aplicativo para gerar um código Morse, decodificar e escutar esse código",
            "infoText": "Escreva a mensagem a ser códificada em código Morse",
            "textBtn": "Codificar Mens",
            "titleFrame2": "Mensagem em Código Morse",
            "playsoundsBtn": "Tocar Código Morse",
            "radioCode": "Codificar",
            "radioDecode": "Decodificar"}

langEn = {"language": "English",
          "titleWindow": "",
          "projectTitle": "Encode and Decode Morse Code",
          "instru": "Use this app to generate a Morse code, decode and listen a sound of code",
          "infoText": "Write your message to code to Morse code:",
          "textBtn": "Encode Message",
          "titleFrame2": "Message in Morse Code",
          "playsoundsBtn": "Play Morse Code",
          "radioCode": "Code",
          "radioDecode": "Decode"}
# END LANG VAR


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
    morseCodeTxBox.delete('1.0', 'end')
    textEntry = textToConvertEn.get()
    codeMorse = encodeMorse.encodeMorse(textEntry)
    morseCode.set(codeMorse)
    morseCodeTxBox.insert(END, codeMorse)


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


def radioSelection():
    global lang, langEn, langPtBr
    if(str(optionVar.get()) == 'decode' and lang == langEn["language"]):
        txtBtn.set(str(langEn["textBtn"]))
        encodeBtn['textvariable'] = txtBtn
        encodeBtn['command'] = decodingMorse
    elif(str(optionVar.get()) == 'decode' and lang == langPtBr["language"]):
        txtBtn.set(langPtBr["textBtn"])
        encodeBtn['textvariable'] = txtBtn
        encodeBtn['command'] = decodingMorse
    elif(str(optionVar.get()) == 'code' and lang == langEn["language"]):
        txtBtn.set(langEn["textBtn"])
        encodeBtn['textvariable'] = txtBtn
        encodeBtn['command'] = encodingMorse
    elif(str(optionVar.get()) == 'code' and lang == langPtBr["language"]):
        txtBtn.set(langPtBr["textBtn"])
        encodeBtn['textvariable'] = txtBtn
        encodeBtn['command'] = encodingMorse
    else:
        print("Error!")


def changeLanguage(choise):
    global lang, langPtBr, langEn
    lang = choise
    if(choise == langPtBr["language"]):
        projectTitleTxt.set(langPtBr["projectTitle"])
        instruTxt.set(langPtBr["instru"])
        infoTextTxt.set(langPtBr["infoText"])
        radioCode.set(langPtBr["radioCode"])
        radioDecode.set(langPtBr["radioDecode"])
        txtBtn.set(langPtBr["textBtn"])
        titleFrame2Txt.set(langPtBr["titleFrame2"])
        playsoundsBtn['textvariable'] = playsoundsBtnTxt.set(
            langPtBr["playsoundsBtn"])

    elif(choise == langEn["language"]):
        projectTitleTxt.set(langEn["projectTitle"])
        instruTxt.set(langEn["instru"])
        infoTextTxt.set(langEn["infoText"])
        radioCode.set(langEn["radioCode"])
        radioDecode.set(langEn["radioDecode"])
        txtBtn.set(langEn["textBtn"])
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

langList = [langPtBr["language"], langEn["language"]]
langSelected = StringVar(inicialScreen, "Language")
print(langList)

langSelect = OptionMenu(frame, langSelected, *langList, command=changeLanguage)
langSelect.grid(columns=1, row=0, padx=10, pady=10)

instrucLb = Label(frame, textvariable=instruTxt,
                  font=('Arial normal', 12))
instrucLb.grid(columns=2, row=1, padx=10, pady=10)

infoTextLb = Label(frame, textvariable=infoTextTxt)
infoTextLb.grid(columns=1, row=2, padx=10, pady=10)

textToConvertEn = Entry(frame, width=100)
textToConvertEn.grid(column=1, row=2, padx=20, pady=20)
optionVar = StringVar(None, 'code')
Radiobutton(frame, value='code', variable=optionVar, textvariable=radioCode, command=radioSelection).grid(
    column=0, row=3, padx=10, pady=10)
Radiobutton(frame, value='decode', variable=optionVar, textvariable=radioDecode, command=radioSelection).grid(
    column=1, row=3, padx=10, pady=10)

encodeBtn = Button(frame, textvariable=txtBtn, command=encodingMorse)
encodeBtn.grid(column=2, row=3, padx=10, pady=10)


"""
    Second frame components
"""
titleFrame2 = Label(frame2, textvariable=titleFrame2Txt)
titleFrame2.grid(column=1, row=4, padx=10, pady=10)
morseCode = StringVar()
morseCodeTxBox = Text(frame2, height=5, width=100,
                      bg="light cyan")
morseCodeTxBox.grid(column=1, row=6, padx=20, pady=20)
"""
        Comando de tocar quase completo. Precisa ajustar.
"""
playsoundsBtn = Button(frame2, textvariable=playsoundsBtnTxt,
                       command=decodingMorseToSong)
playsoundsBtn.grid(column=2, row=6)

inicialScreen.mainloop()
