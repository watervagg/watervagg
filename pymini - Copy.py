import time
import images
import random
import datetime
from datetime import date
# ! i = 1 doesn't work for some reason!
i = 1
# * This is an operating system with a few apps!
# TODO Make more apps 
# TODO Make among us game!
# ! made 1
today = date.today()
currentDT = datetime.datetime.now()


print("\n")
print("%d" % currentDT.hour,":%d" % currentDT.minute,":%d" % currentDT.second)
day = today.strftime("%B %d, %Y")
print("d2 =", day)
print(images.password)
password = input()


# ! Wrong password
if password != "3219":
    print(images.wrongpassword)
    ta = input()


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
                print("Right password plese enter it at the start")


#?Password right
if password == '3219':
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(images.home)
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
                print("You left!")
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
            print(images.calculator)
            print('type leave if you want to leave the calculator (you have to pass every number thought!)')
            num = input("Your number ")
            num2 = input("Your second number ")
            num3 = input("Your third number ")
            num4 = input('do you want "+ - * multiply or / for devide" ')
            if num4 == '+':
                print('the result of', num, '+', num2, '+', num3, 'is', float(num) + float(num2) + float(num3))
            if num4 == '-':
                print('The result is', float(num) - float(num2) - float(num3))
            if num4 == '*':
                print("the result is", float(num) * float(num2) * float(num3))
            if num4 == '/':
                print('the result is', float(num) / float(num2) / float(num3))
            if num.lower() == 'leave' or num2.lower() == 'leave' or num3.lower() == 'leave' or num4.lower() == 'leave':
                print('You have seccesfully left ')
                break
            else:
                print('Invalaid input')
    if main == 'games':
    #*The games folder!
        time.sleep(1)
        print('do you want to play (rock, paper scissors = 1/maths = 2/fast typing = 3/adventure_game = 4/gimbling_game = 5\n/mayse = 6)')
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
                print("You're right! It took you", fin_time, "to reach")
    # if main == 'camera':
    #     import cv2

    #     cap = cv2.VideoCapture(0)

    #     # Check if the webcam is opened correctly
    #     if not cap.isOpened():
    #         raise IOError("Cannot open webcam")

    #     while True:
    #         ret, frame = cap.read()
    #         frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    #         cv2.imshow('Input', frame)

    #         c = cv2.waitKey(1)
    #         if c == 27:
    #             break

    # cap.release()
    # cv2.destroyAllWindows()