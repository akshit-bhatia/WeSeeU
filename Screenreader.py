import pyautogui
import time
import speech_recognition as sr
import subprocess
import pyttsx3

# Initializing TTS engine
engine = pyttsx3.init()
engine.setProperty("rate",130)

# Building an object for Speech recognization
r = sr.Recognizer()  

# Setting up the game path and calling it
Game_path = ".\BallGame.exe"

process = subprocess.Popen(Game_path, stderr = subprocess.PIPE)

time.sleep(2)

# Giving a subtitle file for TTS
text_val = ".\Textfiles\TestfileTTS.txt"
file1 = open(text_val, 'r')
Lines = file1.readlines()
errormessage = "Sorry, I did not get that"
language = 'en'  

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

# building up the cases for selected option of a user
if option == "play":
    x, y = pyautogui.locateCenterOnScreen(".\Images\play1.png", confidence = 0.8)
    pyautogui.moveTo(x, y, 1)
    pyautogui.click()

elif option == "Instruction":
    x, y = pyautogui.locateCenterOnScreen(".\Images\info1.png", confidence = 0.8)
    pyautogui.moveTo(x, y, 1)
    pyautogui.click()

elif option == "High Score":
    x, y = pyautogui.locateCenterOnScreen(".\Images\highscore1.png", confidence = 0.8)
    pyautogui.moveTo(x, y, 1)
    pyautogui.click()

elif option == "Add Score":
    x, y = pyautogui.locateCenterOnScreen(".\Images\addscore.png", confidence = 0.8)
    pyautogui.moveTo(x, y, 1)
    pyautogui.click()

elif option == "exit":
    x, y = pyautogui.locateCenterOnScreen(".\Images\quit1.png", confidence = 0.8)
    pyautogui.moveTo(x, y, 1)
    pyautogui.click()