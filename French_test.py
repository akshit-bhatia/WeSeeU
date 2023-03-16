import pyautogui
import webbrowser
import time
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import simpledialog

# Initializing TTS engine
engine = pyttsx3.init()

engine.setProperty("rate",130)

voices = engine.getProperty('voices')


voice = engine.getProperty('voices')[3] # the french voice
engine.setProperty('voice', voice.id)
lan2 = "My name is Manav"
for voice in voices:
    print("Voice: %s" % voice.name)
    print("\n")
engine.say(lan2)
engine.runAndWait()

         
r = sr.Recognizer() 
text=""

with sr.Microphone() as source:
    print("Talk")
    audio_text1 = r.listen(source)
    print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text1, language="fr-FR")
        print("Text: "+r.recognize_google(audio_text1, language="fr-FR"))
    except:
         engine.say("Sorry")
         engine.runAndWait()

print("Test", text)

if text == "bonjour":
    print("Done")