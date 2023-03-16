

#import webbrowser

#url = 'https://www.crazygames.com/game/stickman-archer-2'

# Windows
#chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'

#webbrowser.get(chrome_path).open(url)

import pyautogui
import time
import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate",130)
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

            