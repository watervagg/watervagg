import datetime
import time


print("Your parents need to enter these things")
time.sleep(1)
alarmHour = int(input("what hour do you want your child to close the computer : "))
alarmMunite = int(input("What minute do you want your child to close ther computer : "))
amPM = str(input("am or pm (Pymini segguest PM) : "))

if (amPM.lower() == "pm"):
    alarmHour = alarmHour + 12

while (1 == 1):
    import pykids
    if (alarmHour == datetime.datetime.now() .hour and
    alarmMunite == datetime.datetime.now() .minute):
        print("Im really sorry but you can't be on pymini any more :(")
        break

print("Im really sorry but you can't be on pymini any more :(")