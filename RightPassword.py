from tkinter import *
from tkinter.ttk import *
import datetime as dt
 
# importing strftime function to
# retrieve system's time
from time import strftime

#TODO make the apps eccept google google is arleady made!


compiler = Tk()
compiler.title('Pymini')
compiler.geometry("1500x500")
# creating tkinter window
def datetime(): 
    date = dt.datetime.now()
    # Create Label to display the Date
    label = Label(compiler, text=f"{date:%A, %B %d, %Y}", font="Calibri, 20")
    label.pack(pady=20, anchor=CENTER) 
    # This function is used to
    # display time on the label
datetime()
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text =string)
    lbl.after(1000, time)
 
# Styling the label widget so that clock
# will look more attractive
lbl = Label(compiler, font = ('calibri', 40, 'bold'),
            background = 'black',
            foreground = 'white')
# Placing clock at the centre
# of the tkinter window
lbl.pack(side=RIGHT)
time()
def GooglePy():
    import google

text = Label(compiler, text="These are all the pymini apps").pack(side=TOP)
google = Button(compiler, text="Google", command=GooglePy).pack(side=TOP)
games = Button(compiler, text="Games(folder)").pack(side=TOP)
Motivation = Button(compiler, text='Motivation').pack(side=TOP)
Demotivation = Button(compiler, text="Demotivation").pack(side=TOP)
Calculator = Button(compiler, text="Calculator")
Calculator.grid(row = 4, column = 4)

compiler.mainloop()
