import time
import images
import random
import datetime
import pyttsx3
from datetime import date
from colorama import init, Fore, Back, Style
i = 1
# * This is an operating system with a few apps!
# TODO Make more apps
# ! made 1
today = date.today()
currentDT = datetime.datetime.now()
password = "3219"

try:
    print(Fore.MAGENTA + "\n")
    print("%d" % currentDT.hour,":%d" % currentDT.minute,":%d" % currentDT.second)
    day = today.strftime("%B %d, %Y")
    print("d2 =", day)
    print(images.password)
    password = input()
    print(Fore.RESET)

    # ! Wrong password
    if password != "3219":
        print(Fore.RED+images.wrongpassword)
        ta = input()


        if ta == "no":
            print("Ok successfully left")
        if ta == 'yes':
            second = input("enter your password ")
            if second != '3219':
                print("You locked the phone wait 20 seconds")
                while i <= 20:
                    time.sleep(1)
                    print(i)
                    i = i + 1
                trird = input("Type your password ")
                if trird != "3219":
                    print("Your phone is locked you dont have an other try!")
                else:
                    print("Ok plese enter it the first time!")
            else:
                    print("Right password plese enter it at the start" + Fore.RESET)
        else:
            print("Can't understand")


        #?Password right
    if password == password or second == password or trird == password:
        while True:
            print(Fore.MAGENTA)
            print(images.background)
            print("%d" % currentDT.hour,":%d" % currentDT.minute,":%d" % currentDT.second)
            main = input()

            # * The notes app!
            if main.lower() == 'notes':
                while True:
                    notes = []
                    print("Press leave to leave notes")
                    print(images.notes)
                    note_w = input(">  ")
                    if note_w != 'leave':
                        notes.append(note_w)
                        print(notes)
                    if note_w.lower() == 'leave':
                        print("You left!"+Fore.RESET)
                        break

            
            # * The proggram app
            if main == 'program':
                print(images.proggram)
                print('type here')
                print('type here')
                print('type here')

            
            # * The calculator app
            if main == 'calculator':
                while True:
                    time.sleep(1)
                    print(Fore.GREEN+images.calculator)
                    print('type leave if you want to leave the calculator (you have to pass every number thought!)')
                    num = float(input("Your number "))
                    num2 = float(input("Your second number "))
                    # num3 = input("Your third number ")
                    num4 = input('do you want "+ - * multiply or / for devide" ')
                    if num4 == '+':
                        print('the result of', num, '+', num2, 'is', (num) + (num2))
                    if num4 == '-':
                        print('The result is', (num) - (num2))
                    if num4 == '*':
                        print("the result is", (num) * (num2))
                    if num4 == '/':
                        print('the result is', (num) / (num2))
                    if num.lower() == 'leave' or num2.lower() == 'leave' or num4.lower() == 'leave':
                        print('You have seccesfully left '+Fore.RESET)
                        break
                    else:
                        print('Invalaid input')
                    
            if main == 'games':
            #*The games folder!
                time.sleep(1)
                print(Fore.LIGHTYELLOW_EX+'do you want to play (rock, paper scissors = 1/maths = 2/fast typing = 3/adventure_game = 4/gimbling_game = 5\n/mayse = 6)')
                game = input()

                # * The adventure_game game
                # ? Im using an other project for this game!
                if game.lower() == 'adventure_game' or game.lower() == '4':
                    print('ok starting')
                    import adventure_game
                

                # * The gimbling_game
                # ! Im using an other project for this game!
                if game.lower() == 'gimbling_game' or game.lower() == '5':
                    print('ok starting')
                    import gimbling_game

                
                
                #? rock, paper, scissors
                if game.lower() == 'rock, paper, scissors' or game.lower() == '1':
                    while True:
                        print('what do you want rock, paper or scissors\nif you want to leave press o')
                        rps = input()
                        ROPESC = ['rock', 'paper', 'scissors']
                        RPS = random.choice(ROPESC)
                        print('the bot chose', RPS)
                        if rps == 'o': 
                            print('You left!')
                            break
                    

                if game == 'maths' or game == '2':
                    Maths = ['4', '79', '89', '57', '8', '7.8', '-2', '69']
                    Maths2 = ['45', ' +3','76', '8.09', '53', '21']
                    Symbols = ['+', '-', '*', '/']

                    symbols = random.choice(Symbols)
                    maths = random.choice(Maths)
                    maths2 = random.choice(Maths2)
                    print('Starting in ')
                    time.sleep(1)
                    print(3)
                    time.sleep(1)
                    print(2)
                    time.sleep(1)
                    print(1)
                    time.sleep(1)
                    print('GO!')
                    start_time = time.time()
                    print('Your porblem is', maths, symbols, maths2, '=')
                    maths = input()
                    fin_time = time.time() - start_time
                    print('It took you', fin_time, 'to figure it out')
                if game == 'fast typing' or game == '3':
                    fastyping = ['cat', 'man', 'woman', 'python', 'VScode', 'easy', 'last']
                    time.sleep(1)
                    print(3)
                    time.sleep(1)
                    print(2)
                    time.sleep(1)
                    print(1)
                    time.sleep(1)
                    print("GO!")
                    fast = random.choice(fastyping)
                    ft = random.choice(fastyping)
                    fasttyping = random.choice(fastyping)
                    start_time = time.time()
                    time.sleep(3)
                    ft = input(fasttyping)
                    time.sleep(1)
                    ft2 = input(fast)
                    time.sleep(0.4)
                    ft3 = input(ft)
                    if ft != fasttyping and ft2 != fast and ft3 != ft:
                        print("You're wrong!")
                    else:
                        fin_time = time.time() - start_time
                        print("You're right! It took you", fin_time, "to reach"+Fore.RESET)
            if main == 'camera':
                import cv2

                cap = cv2.VideoCapture(0)

                # Check if the webcam is opened correctly
                if not cap.isOpened():
                    raise IOError("Cannot open webcam")

                while True:
                    ret, frame = cap.read()
                    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
                    cv2.imshow('Pycamera', frame)

                    c = cv2.waitKey(1)
                    if c == 27:
                        break

                cap.release()
                cv2.destroyAllWindows()
            if main.lower() == 'google':
                print(Fore.RED)
                import google_assistant
                print(Fore.RESET)
            if main.lower() == 'repeat':    
                while True:
                    repeat = input(Fore.YELLOW+"<say something... >$ ")
                    Repeat = pyttsx3.init()
                    Repeat.say(repeat)
                    Repeat.runAndWait()
                    print(Fore.RESET)
            if main.lower() == 'motivation':
                while True:
                    MMotivation = pyttsx3.init()
                    Motivation = ["You are the best proggramer ever", 'everyone loves you', "You're pretty"]
                    motivation = random.choices(Motivation)
                    print(motivation)
                    MMotivation.say(motivation)
                    MMotivation.RunAndWait()
            if main.lower() == 'clock':
                while True:
                    time.sleep(1)
                    currentDT = datetime.datetime.now()
                    print("%d" % currentDT.hour,":%d" % currentDT.minute,":%d" % currentDT.second)
            if main.lower() == "loop" or main.lower() == "turn off infinite feature":
                turn_off = input("Are you sure you want to turn off? (yes/no) : ")
                if turn_off == "no":
                    print("Ok not gonna turn off infinite feature!")
                if turn_off == "yes":
                    print("Successfully turned off!")
                    for i in range(1):
                        import pymini
                        break
                    break
            if main.lower() == 'leave':
                break
            else:
                print("Im really sorry but I can't understand")
                
except Exception:
    print(Fore.BLUE+images.Error+Fore.RESET)
    import load_bar
    import pymini