from logging import root
from tkinter import *

root = Tk()
root.title('Games Folder')
root.geometry('700x350')
root.config(bg='gray')
def Down() : 
    downLine = Label(root, text='\n').pack
Title = Label(root, text="Welcome to the 'Games folder' What do you want to open\n\n\n\n", 
font='Helvetica 18 bold', bg='gray').pack(side=TOP)
rps = Button(root, text="\n    rock, paper, scissors    \n", command="", fg='orange', bg='gray', font='Helvetica 10 bold').pack()
Down()

root.mainloop()
