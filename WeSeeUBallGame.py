# Initial point of code were game starts.

#Importing requried libraries.
import os
import pyttsx3
import sys
import subprocess 
import time
import pyautogui
import tkinter as tk
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
from googletrans import Translator

# Method for objection identification and navigation.
def choice(choices):
 
    if choices== "play" or choices== "nouveau jeu":
        xcoordinate, ycoordinate = pyautogui.locateCenterOnScreen(".\\Images\\NewGame.png", confidence = 0.7)
        pyautogui.moveTo(xcoordinate, ycoordinate,1)
        pyautogui.click()
    
    
    elif choices== "add your scores" or choices== "ajoutez vos notes":
        xcoordinate, ycoordinate = pyautogui.locateCenterOnScreen(".\\Images\\addscores.png", confidence = 0.7)
        pyautogui.moveTo(xcoordinate, ycoordinate,1)
        pyautogui.click()
        

    elif choices== "high scores" or choices== "scores élevés":
        xcoordinate, ycoordinate = pyautogui.locateCenterOnScreen(".\\Images\\HighScores.png", confidence = 0.7)
        pyautogui.moveTo(xcoordinate, ycoordinate,1)
        pyautogui.click()
    

    elif choices== "instruction" or choices== "instruction":
        xcoordinate, ycoordinate = pyautogui.locateCenterOnScreen(".\\Images\\Instruction.png", confidence = 0.7)
        pyautogui.moveTo(xcoordinate, ycoordinate,1)
        pyautogui.click()
        Voice="Pressing Close. Instructions is given in Game"
        speakText(Voice, optedLanguage)
        xcoordinate1, ycoordinate1 = pyautogui.locateCenterOnScreen(".\\Images\\Instruction.png", confidence = 0.7)
        pyautogui.moveTo(xcoordinate1, ycoordinate1,1)
        pyautogui.click()


    elif choices== "exit" or  choices== "sortie":
        xcoordinate, ycoordinate = pyautogui.locateCenterOnScreen(".\\Images\\ExitGame.png", confidence = 0.7)
        pyautogui.moveTo(xcoordinate, ycoordinate,1)
        pyautogui.click()   

# Method to give language coices to user
def speakText(line,optedLanguage = 'en', x=False):
    if optedLanguage =="français":

        line = translator.translate(line, dest = 'fr', tld = x)
        text = line.text
        speak = gTTS(text =text, lang='fr',slow=x )
        speak.save("frenchoutput.mp3")
        playsound('frenchoutput.mp3')
        os.remove('frenchoutput.mp3')
    else:
        speak = gTTS(text =line, lang='en',slow=x )

        speak.save("Englishoutput.mp3")
        playsound('Englishoutput.mp3')
        os.remove('Englishoutput.mp3')

def Go():
    print("in go")
    r=None
    r=pyautogui.locateOnScreen(".\\Images\\Go.png")
    if r is not None:
        print("in go if")
        pyautogui.moveTo(r)
        Voice="You have to press and hold Mouse click and leave when game narrate Relase."
        engine.say(Voice)
        engine.runAndWait() 
    z=None
    z=pyautogui.locateOnScreen(".\\Images\\Release3.png", confidence=0.80)
    if z is not None:
        Voice="Relase Now."
        print(Voice)
        engine.say(Voice)
        engine.runAndWait()
        time.sleep(3)      
        z=pyautogui.locateOnScreen(".\\Images\\FinishGame.png", confidence=0.80)
        pyautogui.moveTo(z)
    
def GameOver():
    r=None
    r=pyautogui.locateOnScreen(".\\Images\\GameOverBallGame.png")
    if r is not None:
        Voice="Game Over."
        speakText(Voice, optedLanguage)   
    sys.exit(0)

# A tuple containing all the language and
# codes of the language will be detcted
languageSet = ('french','fr','english','en')  

# invoking Translator
translator = Translator()

# Building an object for Speech recognization
speechRecognizer = sr.Recognizer() 

engine = pyttsx3.init()
engine.setProperty("rate",170)

Game_path = ".\\BallGame.exe"

process = subprocess.Popen(Game_path, stderr = subprocess.PIPE)

# Allowing user to choose a language
englishLanguage = "If you want to continue in English say English."
speakText(englishLanguage)

frenchLanguage = "Si tu veux continuer en français, dis français."
speakText(frenchLanguage,'français')

initialInput = "initial input"

while(initialInput == "initial input"):
    with sr.Microphone() as source:
        speakText("Talk Now")
        global optedLanguage 
        optedLanguage = speechRecognizer.listen(source)
        speakText("Time Over, Thanks")
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            # using google speech recognition
            print("Text: "+speechRecognizer.recognize_google(optedLanguage))
            initialInput = "ended"
        except:
            speakText("Sorry, I did not get that")

            time.sleep(2)


# This feature will be narrate through cursor reading for selecting words per minute
Voice="Please select the narration speed. Normal or slow"
speakText(Voice, optedLanguage)

initialInput = "initial input"

while(initialInput == "initial input"):
    with sr.Microphone() as source:
        speakText("Talk Now", optedLanguage)
        global optedVoice
        optedVoice = speechRecognizer.listen(source)
        speakText("Time Over, Thanks", optedLanguage)
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

        try:
            # using google speech recognition
            print("Text: "+speechRecognizer.recognize_google(optedVoice))
            initialInput = "ended"
        except:
            speakText("Sorry, I did not get that", optedLanguage)

if optedVoice == "slow": 
    speakText('You have chose slow speed',optedLanguage = 'en', x=True)
else:
     speakText('You have chose normal speed',optedLanguage = 'en', x=False)  


page1 = ".\\Textfiles\\BallGamePage1.txt" 
file1 = open(page1, 'r')
Lines = file1.readlines()

# Creating an object for playing the sound.
for line in Lines:
    speakText(line, optedLanguage)

# Asking user to choose an option and saying it in their microphone
initialInput = "initial input"

while(initialInput == "initial input"):
    with sr.Microphone() as source:
        speakText("Talk Now", optedLanguage)
        optedOption = speechRecognizer.listen(source)
        speakText("Time Over, Thanks", optedLanguage)
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

        try:
            # using google speech recognition
            print("Text: "+speechRecognizer.recognize_google(optedOption))
            initialInput = "ended"
        except:
            speakText("Sorry, I did not get that", optedLanguage)

option = speechRecognizer.recognize_google(optedOption)
choice(option)    

Voice="Please be Ready."
speakText(Voice, optedLanguage) 

input = "started"
while(True):
    while input =="started":
        print("abc")
        try:
            Go()
            GameOver()
        except:
            pass