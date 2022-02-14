import time
import random
import datetime
from datetime import date

from colorama.ansi import Fore
# TODO High score FAIL
# * Game boring but works!
# ? Do you like it?
space = "\n" *10
today = date.today()

while True:
    print(space, '--------------------------------------------------------------')
    high_score = 100
    d2 = today.strftime("%B %d, %Y")
    print(Fore.LIGHTRED_EX + "day =", d2 + Fore.RESET)
    print('\nHello to gambling games')
    print('\nPress s to start, h for help and l for leave!')
    x = input()
    if x == 'h':
        print('this is gamling games')
        print('\nthis game is lucky number if the number are more then 10')
        print('you gain 10 points if its under you lose 10 points')
        print('you have three rounds if you lose you lose 50 points')
        print('if you win you get 50 points')
    if x == 's':
        print('ok')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('GO!')
        li = ['19', '8', '45', '100', '5', '0', '-10', '+50']
        game = random.choice(li)
        game2 = random.choice(li)
        game3 = random.choice(li)
        print('you got', game)
        print('second try is', game2)
        print('third try is' , game3)
        time.sleep(1)
        result = float(game) + float(game2) + float(game3)
        print('that brings you to', result)
        if result > 100:
            win = result + 50
            print('good job you got', result,'points and with 50 more', win)
        if result < 100:
            lose = result - 50
            print('you lose 50 points sorry', lose)
    if x.lower() == 'l' or x.lower() == 'leave':
        print('\n\nYou secesfully left the game!')
        print('Do you want to to go to pymini? (yes/no)')
        pymi = input()
        if pymi.lower() == 'yes':
            import pymini
        if pymi.lower() == 'no':
            print('Ok!')
    break
