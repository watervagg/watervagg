# tese are the requiered libraries you'll need
from tkinter import *
# from tkinter.font import BOLD
import webbrowser as wb

     
# This will create the window
compiler = Tk()
#The title
compiler.title('google')
compiler.geometry('1000x400')
#These are all the defings
#this Opens google
def OpenGoogle():
    # This says webbrower open google.com
    wb.open('https://www.google.com/')
# This defines Search
def GoogleResearch():

    say = Label(compiler, text="Ok What do you wnat to research").pack(side=TOP)

    wdutr = Label(compiler, text='what do you want to research(The link in the terminal) : ').pack(side=TOP)
    #** We can't make you type 
    # on tkinter because we need to say open the site that the user types
    # and with text in tkinter you dont have enter Enter = one line down
    # and there's no Submit **#
    x = input("Type what the website you wnat to go in : ")
    wb.open(x)

#These are all the buttons
google = Label(compiler, text="Google Needs to know waht you want", fg='blue').pack(fill=BOTH,expand=False)
# google.configure(font=("Helvetica",BOLD, 18))#this is not working not making the text as bold
openGoogle = Button(compiler, text="Open google", command=OpenGoogle).pack(side=LEFT)
OpenResearch = Button(compiler, text="Research", command=GoogleResearch).pack(side=RIGHT)
Exit = Button(compiler, text="Exit", command=compiler.destroy).pack(side=BOTTOM)

compiler.mainloop()# _ _ _ _ _ _ _ _