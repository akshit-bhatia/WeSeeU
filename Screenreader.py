import pyautogui
import webbrowser
import time
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import simpledialog



def choices(option):
    if option == "play now":
        x, y = pyautogui.locateCenterOnScreen(".\Images\playnow.png", confidence = 0.8)
        pyautogui.moveTo(x, y, 1)
        pyautogui.click()
    
    elif option == "level 1":
        x, y = pyautogui.locateCenterOnScreen(".\Images\level1.png", confidence = 0.8)
        pyautogui.moveTo(x, y, 1)
        pyautogui.click()


    elif option == "level 2":
        x, y = pyautogui.locateCenterOnScreen(".\Images\level.png", confidence = 0.8)
        pyautogui.moveTo(x, y, 1)
        pyautogui.click()


    elif option == "play":
        x, y = pyautogui.locateCenterOnScreen(".\\Images\\taptoplay.png", confidence = 0.8)
        pyautogui.moveTo(x, y, 1)
        pyautogui.click()

    elif option == "fire":
        x, y = pyautogui.locateCenterOnScreen(".\Images\opponent.png", confidence = 0.8)
        pyautogui.moveTo(x, y, 1)
        pyautogui.click()

    elif option == "fullscreen":
        x, y = pyautogui.locateCenterOnScreen(".\Images\Fullscreen.png", confidence = 0.8)
        pyautogui.moveTo(x, y, 1)
        pyautogui.click()

    elif option == "replay":
        x, y = pyautogui.locateCenterOnScreen(".\Images\Replay.png", confidence = 0.8)
        pyautogui.moveTo(x, y, 1)
        pyautogui.click()
    elif option == "single player" or option == "finger player":
        x, y = pyautogui.locateCenterOnScreen(".\Images\Singleplayer.png", confidence = 0.8)
        pyautogui.moveTo(x, y, 1)
        pyautogui.click()
    

# Initializing TTS engine
engine = pyttsx3.init()

engine.setProperty("rate",130)

        
        



# Building an object for Speech recognization
r = sr.Recognizer()  


# Setting up the game path and calling it
url = 'https://www.crazygames.com/game/stickman-archer-2'

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

webbrowser.get(chrome_path).open(url)

time.sleep(2)


errormessage = "Sorry, I did not get that"
Voice="Please choose a Voice. Male or Female"
engine.say(Voice)
engine.runAndWait()
with sr.Microphone() as source:
    print("Talk")
    audio_text1 = r.listen(source)
    print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        # using google speech recognition
        print("Text: "+r.recognize_google(audio_text1))
    except:
         engine.say(errormessage)
         engine.runAndWait()
voice= r.recognize_google(audio_text1)

if voice=="female":
    voice = engine.getProperty('voices') #get the available voices
    engine.setProperty('voice', voice[1].id)
elif voice == "male":
    voice = engine.getProperty('voices') #get the available voices
    engine.setProperty('voice', voice[0].id)

ROOT = tk.Tk()
ROOT.withdraw()
response = simpledialog.askstring(title="Words Per Minute", prompt = "1. 125 2. 130 3. 175 ")

engine.setProperty("rate",response)

# Giving a subtitle file for TTS
text_val = "Do you want to Play Now?"

engine.say(text_val)
engine.runAndWait()

# Asking user to choose an option and saying it in their microphone
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        # using google speech recognition
        print("Text: "+r.recognize_google(audio_text))
    except:
         #engine.say(errormessage)
         #engine.runAndWait()
        x, y = pyautogui.locateCenterOnScreen(".\Images\playnow.png", confidence = 0.8)
        pyautogui.moveTo(x, y, 1)
        pyautogui.click()

option = r.recognize_google(audio_text)
choices(option)

text_val = ".\Textfiles\Page_1.txt"
file1 = open(text_val, 'r')
Lines = file1.readlines()


# Creating an object for playing the sound
for line in Lines:
    engine.say(line)
    engine.runAndWait()

# Asking user to choose an option and saying it in their microphone
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        # using google speech recognition
        print("Text: "+r.recognize_google(audio_text))
    except:
         engine.say(errormessage)
         engine.runAndWait()

option = r.recognize_google(audio_text)
choices(option)

text_val = ".\Textfiles\Page_2.txt"
file1 = open(text_val, 'r')
Lines = file1.readlines()


# Creating an object for playing the sound
for line in Lines:
    engine.say(line)
    engine.runAndWait()

# Asking user to choose an option and saying it in their microphone
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        # using google speech recognition
        print("Text: "+r.recognize_google(audio_text))
    except:
         engine.say(errormessage)
         engine.runAndWait()
        

option = r.recognize_google(audio_text)
x, y = pyautogui.locateCenterOnScreen(".\\Images\\taptoplay.png", confidence = 0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()


time.sleep(3)


while True:
    try:
        x, y = pyautogui.locateCenterOnScreen(".\Images\opponent.png", confidence = 0.5)
        cursor =pyautogui. position()
        a = cursor[0]
        b = cursor[1]

        relativeA= a-x
        relativeB = b-y
        
        if relativeA in range(-100,100) and relativeB in range(-100,100):
            pyautogui.moveTo(x, y-40, 1)
            trigger="Fire"
            engine.say(trigger)
            engine.runAndWait()
            engine.setProperty("rate",150)
    except:
        pass

r = None
while r is None:
    r = pyautogui.locateOnScreen('.\Images\gameover.png', grayscale = True)
    text_val = ".\Textfiles\Page_4.txt"
    file1 = open(text_val, 'r')
    Lines = file1.readlines()
    # Creating an object for playing the sound
    for line in Lines:
        engine.say(line)
        engine.runAndWait()

    # Asking user to choose an option and saying it in their microphone
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        
        try:
            # using google speech recognition
            print("Text: "+r.recognize_google(audio_text))
        except:
            engine.say(errormessage)
            engine.runAndWait()

    option = r.recognize_google(audio_text)
    choices(option)