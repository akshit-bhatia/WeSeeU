'''''
# Importing necessary modules required
from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
flag = 0
  
# A tuple containing all the language and
# codes of the language will be detcted
dic = ('french','fr','english','en')
  
  
# Capture Voice
# takes command through microphone
def takecommand():  
    r = sr.Recognizer()
    audio = input("Input:")
    print("Recognizing.....")
    query = audio
    print(f"The User said {query}\n")
    return query
  
  
# Input from user
# Make input to lowercase
query = takecommand()
while (query == "None"):
    query = takecommand()
  
  
def destination_language():
    print("Enter the language in which you\
    want to convert : Ex. Hindi , English , etc.")
    print()
      
    # Input destination language in
    # which the user wants to translate
    to_lang = takecommand()
    while (to_lang == "None"):
        to_lang = takecommand()
    to_lang = to_lang.lower()
    return to_lang
  
to_lang = destination_language()
  
# Mapping it with the code
while (to_lang not in dic):
    print("Language in which you are trying\
    to convert is currently not available ,\
    please input some other language")
    print()
    to_lang = destination_language()
  
to_lang = dic[dic.index(to_lang)+1]
  
  
# invoking Translator
translator = Translator()
  
  
# Translating from src to dest
text_to_translate = translator.translate(query, dest=to_lang)
  
text = text_to_translate.text
  
# Using Google-Text-to-Speech ie, gTTS() method
# to speak the translated text into the
# destination language which is stored in to_lang.
# Also, we have given 3rd argument as False because
# by default it speaks very slowly
speak = gTTS(text=text, lang=to_lang, slow=False)
  
# Using save() method to save the translated
# speech in capture_voice.mp3
speak.save("captured_voice.mp3")
  
# Using OS module to run the translated voice.
playsound('captured_voice.mp3')
os.remove('captured_voice.mp3')
  
# Printing Output
print(text)
'''

from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

dic = ('en','fr')
# invoking Translator
translator = Translator()
Voice="Please choose a Voice. Male or Female"
Voice = translator.translate(Voice, dest = 'fr')
text = Voice.text
speak = gTTS(text =text, lang='fr',slow=False )
speak.save("frenchtest.mp3")
playsound('frenchtest.mp3')
os.remove('frenchtest.mp3')