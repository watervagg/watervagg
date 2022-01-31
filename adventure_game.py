import time
import random
import images

print('\n________________________________________________________________________________')
game = input('Do you want to play? (yes/no/help) ')

if game.lower().strip() == 'help':
    print('ok so you have * wich tell you have dangerous is')
    print('the thing you chose!')
    time.sleep(1)
    print('the thing you see on (___/___) do you want this or that?')

if game.lower().strip() == 'no':
    print('Thats too bad')

if game.lower().strip() == 'yes':
    print('Welcome the adventure starts now!')
    time.sleep(1)
    print(3)
    time.sleep(1)
    print('2')
    time.sleep(1)
    print(1)
    time.sleep(1)
    print('GO!')
    print('The adventure starts now!')
    print(images.crossroads)
    direction = input()

    if direction == 'RIGHT':
        print("ok so you are going to the right")
        time.sleep(1)
        print('**')
        time.sleep(1)
        answer = input("Oh no you found a monster do you attac or run?(attac/run)")

        if answer == 'attac':
            print('You are a crazy man')
            print('****')
            print('you lost')
        if answer == 'run':
            print('you made it')
            time.sleep(1)
            print('*')
            time.sleep(1)
            print(images.RIGHT)
            answer = input()

            if answer == 'path':
                print('the path a really dangerous')
                time.sleep(1)
                print('****')
                time.sleep(2)
                print(images.path)
                print('YOU LOST')
            
            if answer == 'climb':
                time.sleep(1)
                print("ok let's see")
                time.sleep(2)
                print('Yea you are right')
                answer = input("There's a bear what do you do? (sprint/hide)")
                
                if answer == 'sprint':
                    print('ITS A HILL WHERE ARE YOU GONNA GO?')
                    time.sleep(1)
                    print('\n***')
                    time.sleep(1)#noise
                    print('\n****')
                    time.sleep(1)
                    print('\n*****')
                    time.sleep(1)
                    print('You lost')

                if answer == 'hide':
                    print('Good choice!')
                    time.sleep(1)
                    print('OH the bear amost found you')
                    time.sleep(1)
                    print('***')
                    time.sleep(2)
                    print('YOU WON!')
    if direction == 'LEFT':
        print('Ok')
        time.sleep(3)
        print("Oh no there's a monster do you attac or run? (run/attac)")
        answeer = input()
        
        if answeer == 'run':
            print("There's not that much space to run so you lose")

        if answeer == 'attac':
            print('ok')
            time.sleep(2)
            print('****')
            time.sleep(3)
            print('You kiiled him good job')
            answeer = input('But now you found a car and the police right next to it waht do you do? (car/run)')
            
            if answeer == 'car':
                time.sleep(4)
                print('the police got you')
                time.sleep(1)
                print('****')
                time.sleep(1)
                print('Game over')

            if answeer == 'run':
                print('ok so you ')
                time.sleep(5)
                print("""    /\    /\ 
                               \__/""")
                print('YOU WIN!')