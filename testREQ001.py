import unittest
from googletrans import Translator
from gtts import gTTS
from pydub import AudioSegment
import os
from pathlib import Path
import soundfile as sf
import numpy as np

class TestGoogleTrans(unittest.TestCase):

    def setUp(self):
        self.translator = Translator()

    def test_translation_fr(self):
        text = "Hello, how are you?"
        result = self.translator.translate(text, src='en', dest='fr')
        self.assertEqual(result.text, "Bonjour comment allez-vous?")

    def test_translation_en(self):
        text = "Bonjour comment allez-vous?"
        result = self.translator.translate(text, src='fr', dest='en')
        self.assertEqual(result.text, "Good morning, how are you doing?")

    def test_language_detection(self):
        text = "Bonjour, comment ça va?"
        result = self.translator.detect(text)
        self.assertEqual(result.lang, "fr")

    def test_pronunciation_fr(self):
        text = "Bonjour, comment ça va?"
        speak = gTTS(text =text, lang='fr',slow=False)
        speak.save("SampleTestOut.mp3")
        audio_file_1, sr_1 = sf.read('SampleTestOut.mp3')
        audio_file_2, sr_2 = sf.read('TestREQ001audio.mp3')
        # Compare the two audio files
        if np.array_equal(audio_file_1, audio_file_2):
            print("The two audio files are the same.")
        else:
            print("The two audio files are different.")
        os.remove("SampleTestOut.mp3")

    def test_pronunciation_en(self):
        text = "Good morning, how are you doing?"
        speak = gTTS(text =text, lang='en',slow=False)
        speak.save("SampleTestOut2.mp3")
        audio_file_1, sr_1 = sf.read('SampleTestOut2.mp3')
        audio_file_2, sr_2 = sf.read('TestREQ001audio2.mp3')
        # Compare the two audio files
        if np.array_equal(audio_file_1, audio_file_2):
            print("The two audio files are the same.")
        else:
            print("The two audio files are different.")
        os.remove("SampleTestOut2.mp3")
        
if __name__ == '__main__':
    unittest.main()