import time
import images
import random
# TODO if they type quit and then no go back!
Fast = [115 - 185]
fast = random.choice(Fast)


#The start!
print('welcome to the game')
print(images.car_game)
car = input()

#If they type "quit" everything here will get exicuted!
if car.lower() == 'quit':
    print("Are you sure you want to quit? (yes/no)")
    quit = input()
    if quit == 'yes':
        print("ok you left")
    if quit == 'no':
        print("ok you will be send to the main lobby!")

#This is the actual game
if car.lower() == 'play':
    print("ok starting in ")
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print("GO!")
    #These are the controls
    print("""
    a - accelarate the car
    af - accelarate fast!
    s - stop the car
    r - race
    l - leave
    sl - steer left
    sr - steer right
    b -  go back
    """)
    print(images.race)                                           
    play = input()
    
    #! keys like a s sl sr are beiing exicuted here!
    if play == "a":
        print("car started ready to go!Look at the minimap to see were you want to go")
        play = input(">  ")
        if play == "af":
            print("passing 16th " + fast, "kph")
            play = input(">  ")
            if play == "sr" or play == 'sl':
                print("You're at the city center")
                print(images.high_way)
                play = input(">  ")
                if play == 'a':
                    print("defently going to the high way...")
                    play = input(">  ")
                    if play == 'sl' or play == 'sr':
                        print(images.enter_high_way)
                        play = input(">  ")
                if play == 'a':
                    print(images.minimap)
                    print("defently going to the high way...")
                    if play == 'sl' or play == 'sr':
                        print(images.enter_high_way)
                        print("Plese use af for accelarating fast!")
                        play = input(">  ")
                        if play == 'af':
                            print("we are going super ")