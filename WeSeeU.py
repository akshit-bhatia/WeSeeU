# Initial point of code were game starts.

#Importing requried libraries.
import os
import time
import pyttsx3
import pyautogui
import webbrowser
import tkinter as tk
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
from googletrans import Translator
from tkinter import simpledialog


# Method for objection identification and navigation.
def choices(option):
    if option == "play now":
        xCoordinate, yCoordinate = pyautogui.locateCenterOnScreen(".\Images\playnow.png", confidence = 0.7)
        pyautogui.moveTo(xCoordinate, yCoordinate, 1)
        pyautogui.click()
    
    elif option == "level 1":
        xCoordinate, yCoordinate = pyautogui.locateCenterOnScreen(".\Images\level1.png", confidence = 0.7)
        pyautogui.moveTo(xCoordinate, yCoordinate, 1)
        pyautogui.click()

    elif option == "level 2":
        xCoordinate, yCoordinate = pyautogui.locateCenterOnScreen(".\Images\level.png", confidence = 0.7)
        pyautogui.moveTo(xCoordinate, yCoordinate, 1)
        pyautogui.click()


    elif option == "play":
        xCoordinate, yCoordinate = pyautogui.locateCenterOnScreen(".\\Images\\taptoplay.png", confidence = 0.7)
        pyautogui.moveTo(xCoordinate, yCoordinate, 1)
        pyautogui.click()

    elif option == "fire":
        xCoordinate, yCoordinate = pyautogui.locateCenterOnScreen(".\Images\opponent.png", confidence = 0.7)
        pyautogui.moveTo(xCoordinate, yCoordinate, 1)
        pyautogui.click()

    elif option == "fullscreen":
        xCoordinate, yCoordinate = pyautogui.locateCenterOnScreen(".\Images\Fullscreen.png", confidence = 0.7)
        pyautogui.moveTo(xCoordinate, yCoordinate, 1)
        pyautogui.click()

    elif option == "replay":
        xCoordinate, yCoordinate = pyautogui.locateCenterOnScreen(".\Images\Replay.png", confidence = 0.7)
        pyautogui.moveTo(xCoordinate, yCoordinate, 1)
        pyautogui.click()
    elif option == "single player" or option == "finger player":
        xCoordinate, yCoordinate = pyautogui.locateCenterOnScreen(".\Images\Singleplayer.png", confidence = 0.7)
        pyautogui.moveTo(xCoordinate, yCoordinate, 1)
        pyautogui.click()

# Method to give language coices to user
def speakText(line,optedLanguage):
    if optedLanguage =="français":
        line = translator.translate(line, dest = 'fr')
        text = line.text
        speak = gTTS(text =text, lang='fr',slow=False )
        speak.save("frenchoutput.mp3")
        playsound('frenchoutput.mp3')
        os.remove('frenchoutput.mp3')
    else:
        engine.say(line)
        engine.runAndWait()
    
     
def autoAim(relativeA,relativeB,xCoordinate,yCoordinate,optedLanguage):
        # Autoaim range is defined for cursor
    if relativeA in range(-100,100) and relativeB in range(-100,100):
        pyautogui.moveTo(xCoordinate, yCoordinate-40, 1)
        print("fire")
        trigger="Fire"
        engine.say(trigger)
        engine.runAndWait()
        engine.setProperty("rate",150)

# Initializing Text-To-Speech engine
engine = pyttsx3.init()
engine.setProperty("rate",130)

        
# A tuple containing all the language and
# codes of the language will be detcted
languageSet = ('french','fr','english','en')  

# invoking Translator
translator = Translator()

# Building an object for Speech recognization
speechRecognizer = sr.Recognizer()  

# Setting up the game path and calling it
gameURL = 'https://www.crazygames.com/game/stickman-archer-2'

#Setting up the google driver
chromePath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chromePath).open_new(gameURL)

print("Reached")
# Allowing user to choose a language
englishLanguage = "If you want to continue in English say English."
engine.say(englishLanguage)
engine.runAndWait()

voice = engine.getProperty('voices')[3] # the french voice
engine.setProperty('voice', voice.id)
frenchLanguage = "Si tu veux continuer en français, dis français."
engine.say(frenchLanguage)
engine.runAndWait()

initialInput = "initial input"

while(initialInput == "initial input"):
    with sr.Microphone() as source:
        engine.say("Talk Now")
        engine.runAndWait()
        optedLanguage = speechRecognizer.listen(source)
        engine.say("Time Over, Thanks")
        engine.runAndWait()
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

        try:
            # using google speech recognition
            print("Text: "+speechRecognizer.recognize_google(optedLanguage))
            initialInput = "ended"
        except:
                engine.say("Sorry, I did not get that")
                engine.runAndWait()

if optedLanguage=="English":
    voice = engine.getProperty('voices') #get the available voices
    engine.setProperty('voice', voice[0].id)
elif optedLanguage == "français":
    voice = engine.getProperty('voices')[3] # the french voice
    engine.setProperty('voice', voice.id)


time.sleep(2)

# Allowing User to choose prefferable voice
Voice="Please choose a Voice. Male or Female"
speakText(Voice, optedLanguage)

initialInput = "initial input"

while(initialInput == "initial input"):
    with sr.Microphone() as source:
        engine.say("Talk Now")
        engine.runAndWait()
        optedVoice = speechRecognizer.listen(source)
        engine.say("Time Over, Thanks")
        engine.runAndWait()
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

        try:
            # using google speech recognition
            print("Text: "+speechRecognizer.recognize_google(optedVoice))
            initialInput = "ended"
        except:
                engine.say("Sorry, I did not get that")
                engine.runAndWait()
                
if optedVoice=="female" or "femelle":
    voice = engine.getProperty('voices') #get the available voices
    engine.setProperty('voice', voice[1].id)
elif optedVoice == "male" or "mâle":
    voice = engine.getProperty('voices') #get the available voices
    engine.setProperty('voice', voice[0].id)

# This feature will be narrate through cursor reading for selecting words per minute
ROOT = tk.Tk()
ROOT.withdraw()
wordPace = simpledialog.askstring(title="Words Per Minute", prompt = "1. 125 2. 130 3. 175 ")
engine.setProperty("rate",wordPace)

# Giving a subtitle file for Text-To-Speech
playButton = "Do you want to Play Now?"
speakText(playButton, optedLanguage)

# Asking user to choose an option and saying it in their microphone
initialInput = "initial input"

while(initialInput == "initial input"):
    with sr.Microphone() as source:
        engine.say("Talk Now")
        engine.runAndWait()
        optedOption = speechRecognizer.listen(source)
        engine.say("Time Over, Thanks")
        engine.runAndWait()
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

        try:
            # using google speech recognition
            print("Text: "+speechRecognizer.recognize_google(optedOption))
            initialInput = "ended"
        except:
                engine.say("Sorry, I did not get that")
                engine.runAndWait()


option = speechRecognizer.recognize_google(optedOption)
choices(option)

# Calling Page 1 of the game to narrate the script and user menu.
page1 = ".\Textfiles\Page_1.txt" 
file1 = open(page1, 'r')
Lines = file1.readlines()

# Creating an object for playing the sound.
for line in Lines:
    speakText(line, optedLanguage)

# Asking user to choose an option and saying it in their microphone
initialInput = "initial input"

while(initialInput == "initial input"):
    with sr.Microphone() as source:
        engine.say("Talk Now")
        engine.runAndWait()
        optedOption = speechRecognizer.listen(source)
        engine.say("Time Over, Thanks")
        engine.runAndWait()
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

        try:
            # using google speech recognition
            print("Text: "+speechRecognizer.recognize_google(optedOption))
            initialInput = "ended"
        except:
                engine.say("Sorry, I did not get that")
                engine.runAndWait()

option = speechRecognizer.recognize_google(optedOption)
choices(option) # choices() for object identification

# Calling Page 2 of the game to narrate the script and user menu
page2 = ".\Textfiles\Page_2.txt"
file1 = open(page2, 'r')
Lines = file1.readlines()


# Creating an object for playing the sound
for line in Lines:
    speakText(line, optedLanguage)

# Asking user to choose an option and saying it in their microphone
initialInput = "initial input"

while(initialInput == "initial input"):
    with sr.Microphone() as source:
        engine.say("Talk Now")
        engine.runAndWait()
        optedOption = speechRecognizer.listen(source)
        engine.say("Time Over, Thanks")
        engine.runAndWait()
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

        try:
            # using google speech recognition
            print("Text: "+speechRecognizer.recognize_google(optedOption))
            initialInput = "ended"
        except:
                engine.say("Sorry, I did not get that")
                engine.runAndWait()
        

option = speechRecognizer.recognize_google(optedOption)
xCoordinate, yCoordinate = pyautogui.locateCenterOnScreen(".\\Images\\taptoplay.png", confidence = 0.7)
pyautogui.moveTo(xCoordinate, yCoordinate, 1)
pyautogui.click()


time.sleep(3)

# Auto aiming features for game to target opponent
while True:
    try:
        xCoordinate, yCoordinate = pyautogui.locateCenterOnScreen(".\Images\opponent.png", confidence = 0.7)
        cursor =pyautogui. position()
        a = cursor[0]
        b = cursor[1]
        relativeA= a-xCoordinate
        relativeB = b-yCoordinate
        relativeAx= a-xCoordinate
        relativeBy = b-yCoordinate
        xNew = xCoordinate
        yNew = yCoordinate
        
        time.sleep(2)
        
        autoAim(relativeAx,relativeBy,xCoordinate,yCoordinate,optedLanguage)
        # Navigation aid to detect the location of enemies
        if xCoordinate!= xNew:
            autoAim(relativeAx,relativeBy,xCoordinate,yCoordinate,optedLanguage)
            pass
        else:
            
            if relativeA>0 and relativeB>0:
                
                Northwest = "EnEmies in Northwest"    # Navigation for enimies in Northwest
                speakText(Northwest, optedLanguage)
                autoAim(relativeAx,relativeBy,xCoordinate,yCoordinate,optedLanguage)

                
            elif relativeA<0 and relativeB>0:
                
                Northeast = "EnEmies in Northeast"    # Navigation for enimies in Northeast
                speakText(Northeast, optedLanguage)
                autoAim(relativeAx,relativeBy,xCoordinate,yCoordinate,optedLanguage)

            elif relativeA>0 and relativeB<0:
                
                southwest = "EnEmies in southwest"    # Navigation for enimies in southwest
                speakText(southwest, optedLanguage)
                autoAim(relativeAx,relativeBy,xCoordinate,yCoordinate,optedLanguage)
            
            elif relativeA<0 and relativeB<0:
                
                souteast = "EnEmies in souteast"      # Navigation for enimies in southeast
                speakText(souteast, optedLanguage)
                autoAim(relativeAx,relativeBy,xCoordinate,yCoordinate,optedLanguage)
            autoAim(relativeAx,relativeBy,xCoordinate,yCoordinate,optedLanguage)

                
                
        # Autoaim range is defined for cursor
            
    except:
        pass
        '''
        page4 = ".\Textfiles\Page_4.txt"
        file1 = open(page4, 'r')
        Lines = file1.readlines()
        # Creating an object for playing the sound
        for line in Lines:
            engine.say(line)
            engine.runAndWait()

        # Asking user to choose an option and saying it in their microphone
        with sr.Microphone() as source:
            print("Talk")
            optedOption = speechRecognizer.listen(source)
            print("Time over, thanks")
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
            
            try:
                # using google speech recognition
                print("Text: "+speechRecognizer.recognize_google(optedOption))
            except:
                engine.say("Sorry, I did not get that")
                engine.runAndWait()

        option = speechRecognizer.recognize_google(optedOption)
        choices(option)
        '''
        
