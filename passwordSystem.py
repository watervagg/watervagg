from re import L
from tkinter import *
# import time
import random

passwordText = ["hello", "pymini", "Me", "Im The best", "Click me"]
PasswordText = random.choice(passwordText)
PasswordText2 = random.choice(passwordText)
PasswordText3 = random.choice(passwordText)

#The window
compiler = Tk()
compiler.title("Pymini in animation")


def rightPassword():
    import RightPassword

passwordText = Label(compiler, text="What is your password?")
#The password choices
password1 = Button(compiler, text=PasswordText)

password2 = Button(compiler, text=PasswordText2, command="")

password3 = Button(compiler, text=PasswordText3)

passwordText.pack()
password1.pack()
password2.pack()
password3.pack()
compiler.mainloop()