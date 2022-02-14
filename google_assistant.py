import webbrowser
import pyttsx3
import time
import wikipedia
import pyjokes
from googlesearch import search
from tkinter import *

#googlesearch = speak!
googlesearch = pyttsx3.init()


#This runs for ever
while True:


    ask = input("$ ")
    googlesearch.say("Ok here's what I found")
    #This is ehat it says run and wait
    googlesearch.runAndWait()

    #Wiki
    if ask.lower() == "wikipedia" or ask.lower() == "wiki":
        #webbrower opens the url
        webbrowser.open("https://en.wikipedia.org/wiki/Main_Page/.....")
        break
    
    #YouTube
    if ask.lower() == "youtube":
        #Opens YouTube
        webbrowser.open("https://www.youtube.com/")
        break
    
    #amazon
    if ask.lower() == "amazon":
        #Opens amazon
        webbrowser.open("https://www.amazon.co.uk/")
        break
    
    #Monkey type/typing test
    if ask.lower() == "typing test":
        #Opens monkeytype/typing test
        webbrowser.open("https://monkeytype.com/")
    
    #gmail
    if ask.lower() == "gmail":
        #Opens gmail
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
    
    
    #This is if the users types tell me a joke it tells a joke
    if ask.lower() == "tell me a joke":
        #This runs the jokes 5 times/it says 5 times
        for i in range(5):
            #This creates the joke
            My_joke = pyjokes.get_joke(language="en", category="neutral")

            #This says the joke
            googlesearch.say(My_joke)
            #You can red the joke if your volume is not on
            print(My_joke)
            # * It runs and waits
            googlesearch.runAndWait()
        #It breaks the infite loop because then it gonna go to the links!    
        break
    if ask.lower() == 'repeat what i say':

        #This repeats that
        while True:

            #You type it says!
            talk = input("Say somethig... ")
            #You can leave!
            if talk.lower() == "leave":
                break
            # * Repeats
            googlesearch.say(talk)
            # * Runs and waits
            googlesearch.runAndWait()


    if ask.lower() == 'who is':
        print(wikipedia.search(ask, results="2"))


    for i in search(ask, tld="com", num=5, stop=5, pause=2):
        googlesearch.say(i)
        print(i)
        print("Alt + click to go into the results")
        googlesearch.runAndWait()
    
