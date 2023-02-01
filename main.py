from tkinter import *
from tkinter import ttk

import encodeMorse

inicialScreen = Tk()
inicialScreen.title("Encode and Decode Morse Code")

frame = ttk.Frame(inicialScreen, padding=20)
frame.grid()
ttk.Label(frame,
          text="Encode and Decode Morse Code",
          font=('Arial Bold', 20)
          ).grid(columns=2, row=0)

Label(frame, text="Use this app to generate a Morse code, decode and listen a sound of code",
      font=('Arial normal', 12)).grid(columns=2, row=1, padx=10, pady=10)
infoText = Label(frame, text="Write your message to code to Morse code:").grid(
    columns=1, row=2, padx=10, pady=10)
textToConvert = Entry(frame, width=100).grid(column=1, row=2, padx=20, pady=20)

inicialScreen.mainloop()