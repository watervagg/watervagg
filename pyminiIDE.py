from email.mime import base
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
from turtle import title

compiler = Tk()
compiler.title('Pymini IDE')
file_path = ''



def set_file_path(path):
    global file_path
    file_path = path


def HtmlTutorial() :
    root = Tk()
    root.title('HTMLTutorial')
    titleLabel = Label(root, text="""

\n\n\n\n
    HTML stands for HyperText Markup Language. It is used to design web pages using a markup language. It is the combination of Hypertext and Markup language. 
    Hypertext defines the link between the web pages. A markup language is used to define the text document within tag which defines the structure of web pages. 
    It is a markup language that is used by the browser to manipulate text, images, and other content to display in the required format.
    """)
    BaseOfHTML = Label(root, text="""
    \n\n\n
    Why to use HTML ?
It helps to structure our website well. The way a skeleton system gives a structure to the human body, in a similar manner, it acts as a skeleton for a website, 
without it a website cannot be made. If you want to work as a Software Developer especially in the Web Development domain, then learning HTML is a must, because without knowledge of it you cannot build a website.

Base for creating websites: It is the basic necessity a developer should know while building a website from scratch.
Learn web development: It is the first step towards learning Web Development. Once you learn it, you can build simple,
static websites very easily.
Can become freelancer: Since web development has the best scope in freelancing, therefore learning it will
surely help you to get the best deals of website development in the market.
 

Basic Format: It is the basic format of create a simple web page.

<!DOCTYPE html>
<html>
 
<head>
    <!-- Head section of website-->
    <title></title>
</head>
 
<body>
    <!-- Body section of website -->
</body>
 
</html><div class="open_grepper_editor" title="Edit & Save To Grepper"></div>
Example: Let’s see a small example of simple web page that display the heading and paragraph content.

<!DOCTYPE html>
<html>
 
<head>
    <title>Simple Web Page</title>
</head>
 
<body>
    <h1>Welcome to GeeksforGeeks</h1>
    <p>A computer science portal for geeks</p>
</body>
 

""", font='Helvetica 5 bold')
    titleLabel.pack()
    BaseOfHTML.pack()
def PythonTutorial() :
    root = Tk()
    root.title('Python tutorial')
    BaseOfPython = Label(root, text="""

\n\n\n\n
    Python uses indentation to highlight the blocks of code. Whitespace is used for indentation in Python.
    All statements with the same distance to the right belong to the same block of code. If a block has to be more deeply nested,
    it is simply indented further to the right. You can understand it better by looking at the following lines of code.

    # Python program showing 
    # indentation 
    
    site = 'gfg'
    
    if site == 'gfg': 
        print('Logging on to pymini...') 
    else: 
        print('retype the URL.') 
    print('All set !') 
    Comments are useful information that the developers provide to make the reader understand the source code.
    It explains the logic or a part of it used in the code. There are two types of comment in Python:

    Single line comments: Python single line comment starts with hashtag symbol with no white spaces.
    # This is a comment 
    # Print “pymini !” to console 
    print("Pymini")
    Multi-line string as comment: Python multi-line comment is a piece of text enclosed in a delimiter (“””) on each end of the comment.

    """
    """
    This would be a multiline comment in Python that 
    spans several lines and describes geeksforgeeks. 
    A Computer Science portal for geeks. It contains  
    well written, well thought  
    and well-explained computer science  
    and programming articles,  
    quizzes and more.  
    … 
    print("pymini")

    Variables in Python are not “statically typed”. We do not need to declare variables
    before using them or declare their type.
    A variable is created the moment we first assign a value to it.

    #!/usr/bin/python 
    
    # An integer assignment 
    age = 45                     
    
    # A floating point 
    salary = 1456.8            
    
    # A string   
    name = "John"             
    
    print(age) 
    print(salary) 
    print(name) 

    Operators are the main building block of any programming language. Operators 
    allow the programmer to perform different kinds of operations on operands.
    These operators can be categorized based upon their different functionality:

    Arithmetic operators: Arithmetic operators are used to perform mathematical operations like addition, subtraction,
    multiplication and division.
    # Examples of Arithmetic Operator 
    a = 9
    b = 4
    
    # Addition of numbers 
    add = a + b 
    # Subtraction of numbers  
    sub = a - b 
    # Multiplication of number  
    mul = a * b 
    # Division(float) of number  
    div1 = a / b 
    # Division(floor) of number  
    div2 = a // b 
    # Modulo of both number 
    mod = a % b 
    
    # print results 
    print(add) 
    print(sub) 
    print(mul) 
    print(div1) 
    print(div2) 
    print(mod)
 
    """, font='Helvetica 15 bold')

    BaseOfPython.pack()

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



HelpMenu = Menu(menu_bar, tearoff=0)
HelpMenu.add_command(label='Get started', command=OpenGetStarted)
HelpMenu.add_command(label='', command=OpenMyThemes)
menu_bar.add_cascade(label='Help', menu=HelpMenu)

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()

compiler.mainloop()
