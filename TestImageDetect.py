import os
import time
import pyautogui
import webbrowser
import tkinter as tk
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
from googletrans import Translator
from tkinter import simpledialog



def choice(choices):
 
    if choices== "play now" or choices== "joue maintenant":
        xcoordinate, ycoordinate = pyautogui.locateCenterOnScreen(".\Images\playnow.png", confidence = 0.7)
        pyautogui.moveTo(xcoordinate, ycoordinate,1)
        pyautogui.click()
    
    
    elif choices== "level 1" or choices== "niveau 1":
        xcoordinate, ycoordinate = pyautogui.locateCenterOnScreen(".\Images\level1.png", confidence = 0.7)
        pyautogui.moveTo(xcoordinate, ycoordinate,1)
        pyautogui.click()
        

    elif choices== "level 2" or choices== "niveau 2":
        xcoordinate, ycoordinate = pyautogui.locateCenterOnScreen(".\Images\level.png", confidence = 0.7)
        pyautogui.moveTo(xcoordinate, ycoordinate,1)
        pyautogui.click()
    

    elif choices== "play" or choices== "appuyez pour jouer":
        xcoordinate, ycoordinate = pyautogui.locateCenterOnScreen(".\\Images\\taptoplay.png", confidence = 0.7)
        pyautogui.moveTo(xcoordinate, ycoordinate,1)
        pyautogui.click()


    elif choices== "fire" or  choices== "feu":
        xcoordinate, ycoordinate = pyautogui.locateCenterOnScreen(".\Images\opponent.png", confidence = 0.7)
        pyautogui.moveTo(xcoordinate, ycoordinate,1)
        pyautogui.click()


    elif choices== "fullscreen" or  choices== "plein écran":
        xcoordinate, ycoordinate = pyautogui.locateCenterOnScreen(".\Images\Fullscreen.png", confidence = 0.7)
        pyautogui.moveTo(xcoordinate, ycoordinate,1)
        pyautogui.click()


    elif choices== "replay"or choices=="rejouer":
        xcoordinate, ycoordinate = pyautogui.locateCenterOnScreen(".\Images\Replay.png", confidence = 0.7)
        pyautogui.moveTo(xcoordinate, ycoordinate,1)
        print("Hello Inside replay")
        pyautogui.click()


    elif choices== "single player" or  choices== "joueur unique":
        xcoordinate, ycoordinate = pyautogui.locateCenterOnScreen(".\Images\Singleplayer.png", confidence = 0.6)
        pyautogui.moveTo(xcoordinate, ycoordinate,1)
        pyautogui.click()

    elif choices== "home" or choices== "maison":
        xcoordinate, ycoordinate = pyautogui.locateCenterOnScreen(".\Images\home.png", confidence = 0.7)
        pyautogui.moveTo(xcoordinate, ycoordinate,1)
        pyautogui.click()
    
    elif choices== "mute" or choices== "muette" or choices== "muet":
        xcoordinate, ycoordinate = pyautogui.locateCenterOnScreen(".\Images\mute.png", confidence = 0.7)
        pyautogui.moveTo(xcoordinate, ycoordinate,1)
        pyautogui.click()


def detectAd():
    r=None
    r=pyautogui.locateOnScreen(".\Images\skipad.png")
    print(r)
    if r is not None:
        pyautogui.click(r)

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
    
     
def autoAim(relativeA,relativeB,xCoordinate,yCoordinate,optedLanguage):
    # Autoaim range is defined for cursor
    if relativeA in range(-100,100) and relativeB in range(-100,100):
        pyautogui.moveTo(xCoordinate, yCoordinate-40, 1)
        print("fire")
        trigger="Fire"
        speakText(trigger,optedLanguage)


def detectGameOver():
    r=None
    r=pyautogui.locateOnScreen(".\Images\Replay.png")
    print(r)
    if r is not None:
        page4 = ".\Textfiles\Page_4.txt"
        file1 = open(page4, 'r')
        Lines = file1.readlines()
        # Creating an object for playing the sound
        for line in Lines:
            speakText(line,optedLanguage = 'en', x=False)

        
        initialInput = "initial input"

        while(initialInput == "initial input"):
            with sr.Microphone() as source:
                speakText("Talk Now", optedLanguage='en')
                optedOption = speechRecognizer.listen(source)
                speakText("Time Over, Thanks", optedLanguage='en')
                # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

                try:
                    # using google speech recognition
                    print("Text: "+speechRecognizer.recognize_google(optedOption))
                    initialInput = "ended"
                except:
                    speakText("Sorry, I did not get that", optedLanguage='en')
        option = speechRecognizer.recognize_google(optedOption)
        choice(option)
    
    
languageSet = ('french','fr','english','en')  

# invoking Translator
translator = Translator()

# Building an object for Speech recognization
speechRecognizer = sr.Recognizer()  


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

        detectAd()
        autoAim(relativeAx,relativeBy,xCoordinate,yCoordinate,optedLanguage='en')
        detectGameOver()
        # Navigation aid to detect the location of enemies
        if xCoordinate!= xNew:
            detectAd()
          
            autoAim(relativeAx,relativeBy,xCoordinate,yCoordinate,optedLanguage='en')
            detectGameOver()
            detectAd()
            
            pass
        else:
            
            if relativeA>0 and relativeB>0:
                
                Northwest = "EnEmy in Northwest"    # Navigation for enimies in Northwest
                speakText(Northwest, optedLanguage='en')
                #detectAd()
                #detectGameOver()
                autoAim(relativeAx,relativeBy,xCoordinate,yCoordinate,optedLanguage='en')
               

                
            elif relativeA<0 and relativeB>0:
                
                Northeast = "EnEmy in Northeast"    # Navigation for enimies in Northeast
                speakText(Northeast, optedLanguage='en')
                #detectAd()
                #detectGameOver()
                autoAim(relativeAx,relativeBy,xCoordinate,yCoordinate,optedLanguage='en')
               

            elif relativeA>0 and relativeB<0:
                
                southwest = "EnEmy in southwest"    # Navigation for enimies in southwest
                speakText(southwest, optedLanguage='en')
                #detectAd()
                #detectGameOver()
                autoAim(relativeAx,relativeBy,xCoordinate,yCoordinate,optedLanguage='en')
            
            
            elif relativeA<0 and relativeB<0:
                
                souteast = "EnEmy in souteast"      # Navigation for enimies in southeast
                speakText(souteast, optedLanguage='en')
                #detectAd()
                #detectGameOver()
                autoAim(relativeAx,relativeBy,xCoordinate,yCoordinate,optedLanguage='en')
                
            detectAd()
            detectGameOver()
            autoAim(relativeAx,relativeBy,xCoordinate,yCoordinate,optedLanguage='en')
            
           
                
                
        # Autoaim range is defined for cursor
            
    except:
        detectAd()
        detectGameOver()
        pass