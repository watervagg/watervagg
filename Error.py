import tkinter as tk
from tkinter import *



root = Tk()
 
# specify size of window.
root.geometry("350x170")
 
# Create text widget and specify size.
T = Text(root, height = 5, width = 52)
 
# Create label
l = Label(root, text = "404!")
l.config(font =("Courier", 14))
# l.config(bg='white', fg='black', insertbackground='blue')
 
Fact = """                Error             \n                 404             \n            we're really sorry             """

print(Fact) 
# Create button for next text.
b1 = Button(root, text = "ok", command=root.destroy)
 
l.pack()
T.pack()
b1.pack()
 
# Insert The Fact.
T.insert(tk.END, Fact)
root.mainloop()
 