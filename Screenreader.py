import pyautogui
import webbrowser
import time
import speech_recognition as sr
from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
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

        
# A tuple containing all the language and
# codes of the language will be detcted
dic = ('french','fr','english','en')  
# invoking Translator
translator = Translator()


# Building an object for Speech recognization
r = sr.Recognizer()  

translator = Translator()

dic = ('en','fr')
# Setting up the game path and calling it
url = 'https://www.crazygames.com/game/stickman-archer-2'

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

webbrowser.get(chrome_path).open(url)

time.sleep(2)


lan1 = "If you want to continue in English say English."
engine.say(lan1)
engine.runAndWait()

voice = engine.getProperty('voices')[3] # the french voice
engine.setProperty('voice', voice.id)
lan2 = "Si tu veux continuer en français, dis français."
engine.say(lan2)
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
         engine.say("Sorry, I did not get that")
         engine.runAndWait()
if audio_text1=="English":
    voice = engine.getProperty('voices') #get the available voices
    engine.setProperty('voice', voice[0].id)
elif audio_text1 == "français":
    voice = engine.getProperty('voices')[3] # the french voice
    engine.setProperty('voice', voice.id)

time.sleep(2)
Voice="Please choose a Voice. Male or Female"
if audio_text1 =="français":
    Voice = translator.translate(Voice, dest = 'fr')
    text = Voice.text
    speak = gTTS(text =text, lang='fr',slow=False )
    speak.save("frenchtest.mp3")
    playsound('frenchtest.mp3')
    os.remove('frenchtest.mp3')
else:
    engine.say(Voice)
    engine.runAndWait()
with sr.Microphone() as source:
    print("Talk")
    audio_text1 = r.listen(source)
    print("Time over, thanks")# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        # using google speech recognition
        print("Text: "+r.recognize_google(audio_text1))
    except:
         engine.say("Sorry, I did not get that")
         engine.runAndWait()

if voice=="female" or "femelle":
    voice = engine.getProperty('voices') #get the available voices
    engine.setProperty('voice', voice[1].id)
elif voice == "male" or "mâle":
    voice = engine.getProperty('voices') #get the available voices
    engine.setProperty('voice', voice[0].id)

ROOT = tk.Tk()
ROOT.withdraw()
response = simpledialog.askstring(title="Words Per Minute", prompt = "1. 125 2. 130 3. 175 ")

engine.setProperty("rate",response)

# Giving a subtitle file for TTS
text_val = "Do you want to Play Now?"
if audio_text1 =="français":
    text_val = translator.translate(text_val, dest = 'fr')
    text = text_val.text
    speak = gTTS(text =text, lang='fr',slow=False )
    speak.save("frenchtest.mp3")
    playsound('frenchtest.mp3')
    os.remove('frenchtest.mp3')
else:
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
    if audio_text1 =="français":
        line = translator.translate(line, dest = 'fr')
        text = line.text
        speak = gTTS(text =text, lang='fr',slow=False )
        speak.save("frenchtest.mp3")
        playsound('frenchtest.mp3')
        os.remove('frenchtest.mp3')
    else:
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
         engine.say("Sorry, I did not get that")
         engine.runAndWait()

option = r.recognize_google(audio_text)
choices(option)

text_val = ".\Textfiles\Page_2.txt"
file1 = open(text_val, 'r')
Lines = file1.readlines()


# Creating an object for playing the sound
for line in Lines:
    if audio_text1 =="français":
        line = translator.translate(line, dest = 'fr')
        text = line.text
        speak = gTTS(text =text, lang='fr',slow=False )
        speak.save("frenchtest.mp3")
        playsound('frenchtest.mp3')
        os.remove('frenchtest.mp3')
    else:
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
         engine.say("Sorry, I did not get that")
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
        xNew = x
        yNew = y
        
        if x!= xNew:
            pass
        else:
            if relativeA>0 and relativeB>0:
                
                Northwest = "Enimies in Northwest"
                if audio_text1 =="français":
                    Northwest = translator.translate(Northwest, dest = 'fr')
                    text = Northwest.text
                    speak = gTTS(text =text, lang='fr',slow=False )
                    speak.save("Northwest.mp3")
                    playsound('Northwest.mp3')
                    os.remove('Northwest.mp3')
                else:
                    engine.say(Northwest)
                    engine.runAndWait()
            elif relativeA<0 and relativeB>0:
                
                Northeast = "Enimies in Northeast"
                if audio_text1 =="français":
                    Northeast = translator.translate(Northeast, dest = 'fr')
                    text = Northeast.text
                    speak = gTTS(text =text, lang='fr',slow=False )
                    speak.save("Northeast.mp3")
                    playsound('Northeast.mp3')
                    os.remove('Northeast.mp3')
                else:
                    engine.say(Northeast)
                    engine.runAndWait()
            elif relativeA>0 and relativeB<0:
                
                southwest = "Enimies in southwest"
                if audio_text1 =="français":
                    southwest = translator.translate(southwest, dest = 'fr')
                    text = southwest.text
                    speak = gTTS(text =text, lang='fr',slow=False )
                    speak.save("southwest.mp3")
                    playsound('southwest.mp3')
                    os.remove('southwest.mp3')
                else:
                    engine.say(southwest)
                    engine.runAndWait()
            elif relativeA<0 and relativeB<0:
                
                souteast = "Enimies in souteast"
                if audio_text1 =="français":
                    souteast = translator.translate(souteast, dest = 'fr')
                    text = souteast.text
                    speak = gTTS(text =text, lang='fr',slow=False )
                    speak.save("souteast.mp3")
                    playsound('souteast.mp3')
                    os.remove('souteast.mp3')
                else:
                    engine.say(souteast)
                    engine.runAndWait()
        
        
        if relativeA in range(-100,100) and relativeB in range(-100,100):
            pyautogui.moveTo(x, y-40, 1)
            trigger="Fire"
            if audio_text1 =="français":
                line = translator.translate(line, dest = 'fr')
                text = line.text
                speak = gTTS(text =text, lang='fr',slow=False )
                speak.save("frenchtest.mp3")
                playsound('frenchtest.mp3')
                os.remove('frenchtest.mp3')
        else:
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
                engine.say("Sorry, I did not get that")
                engine.runAndWait()

        option = r.recognize_google(audio_text)
        choices(option)