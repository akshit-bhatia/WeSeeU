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


def choices(option):
    if option == "play now":
        xCoordinate, yCoordinate = pyautogui.locateCenterOnScreen(".\Images\playnow.png", confidence = 0.8)
        pyautogui.moveTo(xCoordinate, yCoordinate, 1)
        pyautogui.click()
    
    elif option == "level 1":
        xCoordinate, yCoordinate = pyautogui.locateCenterOnScreen(".\Images\level1.png", confidence = 0.8)
        pyautogui.moveTo(xCoordinate, yCoordinate, 1)
        pyautogui.click()


    elif option == "level 2":
        xCoordinate, yCoordinate = pyautogui.locateCenterOnScreen(".\Images\level.png", confidence = 0.8)
        pyautogui.moveTo(xCoordinate, yCoordinate, 1)
        pyautogui.click()


    elif option == "play":
        xCoordinate, yCoordinate = pyautogui.locateCenterOnScreen(".\\Images\\taptoplay.png", confidence = 0.8)
        pyautogui.moveTo(xCoordinate, yCoordinate, 1)
        pyautogui.click()

    elif option == "fire":
        xCoordinate, yCoordinate = pyautogui.locateCenterOnScreen(".\Images\opponent.png", confidence = 0.8)
        pyautogui.moveTo(xCoordinate, yCoordinate, 1)
        pyautogui.click()

    elif option == "fullscreen":
        xCoordinate, yCoordinate = pyautogui.locateCenterOnScreen(".\Images\Fullscreen.png", confidence = 0.8)
        pyautogui.moveTo(xCoordinate, yCoordinate, 1)
        pyautogui.click()

    elif option == "replay":
        xCoordinate, yCoordinate = pyautogui.locateCenterOnScreen(".\Images\Replay.png", confidence = 0.8)
        pyautogui.moveTo(xCoordinate, yCoordinate, 1)
        pyautogui.click()
    elif option == "single player" or option == "finger player":
        xCoordinate, yCoordinate = pyautogui.locateCenterOnScreen(".\Images\Singleplayer.png", confidence = 0.8)
        pyautogui.moveTo(xCoordinate, yCoordinate, 1)
        pyautogui.click()



engine = pyttsx3.init()
engine.setProperty("rate",130)
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