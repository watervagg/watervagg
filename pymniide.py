from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
from turtle import width

compiler = Tk()
compiler.title('My Fantastic IDE')
file_path = ''


def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)


textEditor = Text(width=400, height=200 )
textEditor.config(bg='#362f2e', fg='#d2ded1', insertbackground='white', font=('georgia 20'))
textEditor.pack()


#  This is the text size
def twenty():
    textEditor.config(width=1000, height=500,  font=('Georgia 20'))
def fifteen():
    textEditor.config(width=1000, height=500, font=('Georgia 15'))
def fourteen():
    textEditor.config(width=1000, height=500, font=('Georgia 14'))
def thirdteen():
    textEditor.config(width=1000, height=500, font=('Georgia 13'))
def twelve():
    textEditor.config(width=1000, height=500, font=('Georgia 12'))
def eleven():
    textEditor.config(width=1000, height=500, font=('Georgia 11'))
def ten():
    textEditor.config(width=1000, height=500, font=('Georgia 10'))
def five():
    textEditor.config(width=1000, height=500, font=('Georgia 5'))
def MyTextSize():
    root = Tk()
    root.title("IDE text size")   
    v = IntVar() 
    Radiobutton(root, text='20', command=twenty, variable=v, value=1).pack(anchor=W)
    Radiobutton(root, text='15', command=fifteen, variable=v, value=2).pack(anchor=W)
    Radiobutton(root, text='14', command=fourteen, variable=v, value=3).pack(anchor=W)
    Radiobutton(root, text='13', command=thirdteen, variable=v, value=4).pack(anchor=W)
    Radiobutton(root, text='12', command=twelve, variable=v, value=5).pack(anchor=W)
    Radiobutton(root, text='11', command=eleven, variable=v, value=6).pack(anchor=W)
    Radiobutton(root, text='10', command=ten, variable=v, value=7).pack(anchor=W)
    Radiobutton(root, text='5', command=five, variable=v, value=8).pack(anchor=W)
    compiler.bind("Ctrl +", command=twenty)
    compiler.mainloop
    compiler.bind("Ctrl -", command=ten)
    compiler.mainloop
    compiler.bind("Ctrl =", command=fifteen)
    compiler.mainloop
    mainloop()

output = Text(height=0)
output.config(bg='#362f2e', fg='#1dd604')
output.pack()

def light():
    textEditor.config(bg='white', fg='black', insertbackground='blue')
def dark():
    textEditor.config(bg='black', fg='red', insertbackground='blue')
def magenta():
    textEditor.config(bg='magenta', fg='yellow', insertbackground='blue')
def HackerMan():
    textEditor.config(bg='black', fg='green', insertbackground='blue')
def yellow():
    textEditor.config(bg='yellow', fg='green', insertbackground='blue')
def OpenMyThemes():
    #This will make an other window
    root = Tk()
    root.title("IDE settings")
    w = Label(root, text='Here are all the themes')
    v = IntVar()
    #*  the choices
    Radiobutton(root, text='light', command=light, variable=v, value=1).pack(anchor=W)
    Radiobutton(root, text='dark', command=dark, variable=v, value=2).pack(anchor=W)
    Radiobutton(root, text='magenta', command=magenta, variable=v, value=3).pack(anchor=W)
    Radiobutton(root, text='hacker theme', command=HackerMan, variable=v, value=4).pack(anchor=W)
    Radiobutton(root, text='yellow', command=yellow, variable=v, value=5).pack(anchor=W)
    mainloop()    


menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()


veiw_bar = Menu(menu_bar, tearoff=0)
veiw_bar.add_command(label='text size', command=MyTextSize)
veiw_bar.add_command(label='themes', command=OpenMyThemes)
menu_bar.add_cascade(label='veiw', menu=veiw_bar)

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()

compiler.mainloop()