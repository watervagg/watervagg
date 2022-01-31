import random
import time
Colors = "Red " "blue " "Black " "green"
i = 1

try:
    print("Welcome to the buttons game")
    print("starting")
    Players = ['YOU', 'not_me', 'dani', 'josh', 'vvv_hello15_xxx']
    players = random.choice(Players)
    print("Players:", Players)
    if players != "YOU":
        colors = random.choice(Colors)
        print(players, "picked", colors)
        Ex_players = random.choice(Players)
        if Ex_players == players:
            time.sleep(1)
            print(players, "Died! (He exploaded!)")
        else:
            time.sleep(1)
            print("He lived!")
    if players == 'YOU':
        print("You got pretty lucky!")
        print("Its not you its ", players)
        print("The colors are:", Colors)
        print("Choose something! ")
        print(Colors)
        while i <= 20:
            choose = input("?: ")
            time.sleep(1)
            print(i)
            print(Colors)
            if choose == Ex_players:
                time.sleep(1)
                print("YOU DED! ")
            i = i + 1
except Exception:
    print("Something went wrong")