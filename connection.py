import random
import time
import images
while True:
    password = "password"
    name = "name"
    i = 1
    print("Welcome to the connection!")
    print("Plese reigster or login (reigster/login/leave)")
    rl = input("$ ")
    if rl == 'register':
        reigsterlist = []
        Name = input("<Please enter your password>$ ")
        Password = input("<Enter your password>$ ")
        time.sleep(1)
        print("If you want save please go to line (9) fore the name and line (10) for the password")
    if rl == 'login':
        time.sleep(1)
        print("First you need to go to line 9 and 10 for the register!")
        time.sleep(1)
        while i <= 5:
            lname = input("Your name$ ")
            if lname == name:
                time.sleep(1)
                print("Your password was successful!")
                lopassword = input("Enter your password$ ")
                i=i+1
                if lopassword == password:
                    print("Your password was successful")
                    break
            if lname != name:
                print("Wrong!")
                if lopassword != password:
                    print("Password wrong!")
                    if i == 5:
                        time.sleep(1)
                        print("You're probably not the actuall owner!")
    if rl == 'leave':
        print("Seccesfully left!")
        break
    else: 
        print("Invalaid Input")