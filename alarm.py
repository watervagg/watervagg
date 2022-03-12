import datetime
import time
import winsound


print("Those are the times")
time.sleep(1)
alarmHour = int(input("what hour do you want to wake up : "))
alarmMunite = int(input("What minute do you want to wake up : "))
alarmSecond = int(input("What second do you want to wake up : "))
amPM = str(input("am or pm : "))

if (amPM.lower() == "pm"):
    alarmHour = alarmHour + 12

while (1 == 1):
    if (alarmHour == datetime.datetime.now() .hour and
    alarmMunite == datetime.datetime.now() .minute and 
    alarmSecond == datetime.datetime.now() .second):
        for i in range(3):
            sound = "welcome."
            flags=winsound.SND_FILENAME
            for i in range(0,10):
                # winsound.PlaySound(sound,flags)
                duration = 1000  # milliseconds
                freq = 440  # Hz
                winsound.Beep(freq, duration)
            for i in range(0,10):
                winsound.PlaySound(sound, flags)
                x = input("type sleep to to wake up : ")
                if x == "sleep":
                    time.sleep(600)
                    break
            # AlarmTalk = pyttsx3.init()
            # AlarmTalk.say("wake up")
            # AlarmTalk.runAndWait()
            print("WAKE UP")
        break
