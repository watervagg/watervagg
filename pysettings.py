
while True:
    #these are really important to make it work
    x = input("do you want display or users? (user/display/leave)")
    if x.lower() == 'user':
        #These are the users
        print("What user are you?\n")
        print("proggraming")
        print("kids mode")
        print("Student")
        user = input("$ ")
    if x.lower() == "display":
        #This is actuallythe settings
        print("What setting do you want?\n")
        print("wallpaper")
        print("talking")
        print("infinite feature off")
    if x.lower() == "leave":
        print("Seccesfully left")
        break
    else:
        print("Im really sorry but i can't understand")