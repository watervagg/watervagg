from distutils import command
import subprocess
from email.mime import base
#This is the most important import in all of the proggram delete that and you will get 60 or more errors
from tkinter import *
from tkinter import font
#This is for the open files close file e.c.t.
from tkinter.filedialog import askopenfilename, asksaveasfilename
from django.forms import FilePathField

#!These are all the libraries you arre going to need

compiler = Tk()
compiler.title('Pymini IDE')
file_path = ''
i = 1

#TODO make an exit button
#TODO Make color codes

def set_file_path(path):
    global file_path
    file_path = path

def EXIT() :
    root = Tk()
    root.title('do you want to exit?')
    Exit = Label(root, text='Do you want to exit?')
    YesExit = Button(root, text='(y)yes', command=compiler.destroy)
    NoExit = Button(root, text='(n)No', command=root.destroy)
    YesExit.pack()
    NoExit.pack()
    Exit.pack()
    root.mainloop()
 
#This is the html tutorial its really long but
def HtmlTutorial() :
    root = Tk()
    root.title('HTMLTutorial')
    from Tutorial import HTMLtitle
    titleLabel = Label(root, text=HTMLtitle)
    from Tutorial import BaseOfHTML
    BaseOfHTML = Label(root, text=BaseOfHTML, font='Helvetica 5 bold')
    titleLabel.pack()
    BaseOfHTML.pack()
def PythonTutorial() :
    from Tutorial import PythonTitle
    root = Tk()
    root.title('python')
    label = Text(root, text=PythonTitle, font='Helvetica 10 bold')
    label.pack()
    root.mainloop()

def OpenGetStarted() :
    root = Tk()
    root.title('Get started with proggraming')
    root.config(bg="blue")
    Title = Label(root, text="You NEED to start proggraming", font='Helvetica 50 bold')
    textForStarting = Label(root, text="""proggraming is really easy to learn
    start with html or Python then step up to Java, C, C++ or C#
    but starting with python means when you are a bigginer its really good but when you become good at python its good for a lot of things one of them isn't video games
    """, font='Helvetica 15 bold')
    HTMLButton = Button(root, text="Start with HTML", command=HtmlTutorial)
    PythonButton = Button(root, text="Start with Python", command=PythonTutorial)
    Title.config(bg="blue", fg="white")
    textForStarting.config(bg="blue", fg="white")
    HTMLButton.config(bg="RED", fg="white")
    PythonButton.config(bg="GREEN", fg="white")
    Title.pack()
    textForStarting.pack()
    HTMLButton.pack()
    PythonButton.pack()
def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py'), ("HTM5 Files", "*.html"), ("C Files", "*.c"), ("C++ Files", "*.cpp"), ("css Files", "*.css"), ("JavaScript Files", "*.js")])
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
    root = Tk()
    root.title('run')
    label = Label(root, text="Please type this on windows powershell")
    # label2 = Text(root, text=file_path, font='Helvetica 10 bold')
    label.pack()
    # label2.pack()
    root.mainloop()


textEditor = Text(width=400, height=200 )
textEditor.config(bg='#FFFFFF', fg='#000000', insertbackground='#0000FF', font=('georgia 20'))
textEditor.pack()

#  This is the text size
def twentyS(e):
    textEditor.config(width=1000, height=500,  font=('Georgia 20'))
def twenty():
    textEditor.config(width=1000, height=500,  font=('Georgia 20'))
def fifteenS(e):
    textEditor.config(width=1000, height=500, font=('Georgia 15'))
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
def tenS(e):
    textEditor.config(width=1000, height=500, font=('Georgia 10'))
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
    root.bind('<Control-p>', twentyS)
    root.bind('<Control-m>', tenS)
    mainloop()
#these are all the shortcuts
compiler.bind('<Control-p>', twentyS)
compiler.bind('<Control-m>', tenS)
compiler.bind('<Control-l>', fifteenS)


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
def darkPython():
    textEditor.config(bg='gray', fg='#ADD8E6', insertbackground='white')
def lightHTML():
    textEditor.config(bg='white', fg='orange', insertbackground='#ADD8E6')
def lightHTML():
    textEditor.config(bg='gray', fg='orange', insertbackground='#ADD8E6')
def cAndCpp():
    textEditor.config(bg="gray", fg="magenta", insertbackground="black", font=('Helvetica', 15, 'bold'))

def OpenMyThemes():
    #This will make an other window
    root = Tk()
    root.title("IDE settings")
    w = Label(root, text='Here are all the themes')
    v = IntVar()
    #the choices
    Radiobutton(root, text='light', command=light, variable=v, value=1).pack(anchor=W)
    Radiobutton(root, text='dark', command=dark, variable=v, value=2).pack(anchor=W)
    Radiobutton(root, text='magenta', command=magenta, variable=v, value=3).pack(anchor=W)
    Radiobutton(root, text='hacker theme', command=HackerMan, variable=v, value=4).pack(anchor=W)
    Radiobutton(root, text='yellow', command=yellow, variable=v, value=5).pack(anchor=W)
    Radiobutton(root, text='Dark + Python', command=darkPython, variable=v, value=6).pack(anchor=W)
    Radiobutton(root, text='light + html', command=lightHTML, variable=v, value=7).pack(anchor=W)
    Radiobutton(root, text='dark + html', command=lightHTML, variable=v, value=7).pack(anchor=W)
    Radiobutton(root, text='dark + C/C++', command=cAndCpp, variable=v, value=8).pack(anchor=W)
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

HelpMenu = Menu(menu_bar, tearoff=0)
HelpMenu.add_command(label='Get started', command=OpenGetStarted)
HelpMenu.add_command(label='')
menu_bar.add_cascade(label='Help', menu=HelpMenu)

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Do you want to exit?', command=EXIT)
menu_bar.add_cascade(label='Exit', menu=run_bar)

compiler.config(menu=menu_bar)

menu_bar.add_cascade(label="                                                                                                                                                ")
menu_bar.add_cascade(label="Pymini IDE", font=('Helvetica', 15, 'bold'))

editor = Text()
editor.pack()




code_output = Text(height=10)
code_output.pack()

compiler.mainloop()
