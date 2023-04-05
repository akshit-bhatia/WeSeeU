import unittest
from gtts import gTTS
from io import BytesIO
from playsound import playsound
import os
import time
import speech_recognition as sr
from pydub import AudioSegment


class TestGTTS(unittest.TestCase):

    def test_single_language_conversion(self):
        # Test single language conversion (English)
        text = "Hello, how are you?"
        tts = gTTS(text=text, lang="zh")
        audio_file = BytesIO()
        tts.write_to_fp(audio_file)
        audio_file.seek(0)
        self.assertGreater(len(audio_file.read()), 0)
        tts.save("sample.mp3")
        os.system("sample.mp3")
        time.sleep(5)
        os.remove("sample.mp3")
        

    def test_multi_language_conversion(self):
        # Test multi-language conversion (French to English)
        text = "Bonjour, comment ça va?"
        tts_fr = gTTS(text=text, lang="fr")
        audio_file_fr = BytesIO()
        tts_fr.write_to_fp(audio_file_fr)
        audio_file_fr.seek(0)
        self.assertGreater(len(audio_file_fr.read()), 0)
        tts_fr.save("sample.mp3")
        os.system("sample.mp3")
        time.sleep(5)
        os.remove("sample.mp3")
        expected_result = "Hello, how are you?"
        tts_en = gTTS(text=expected_result, lang="en")
        audio_file_en = BytesIO()
        tts_en.write_to_fp(audio_file_en)
        audio_file_en.seek(0)
        self.assertGreater(len(audio_file_en.read()), 0)
        self.assertNotEqual(audio_file_fr.getvalue(), audio_file_en.getvalue())
        tts_en.save("sample.mp3")
        os.system("sample.mp3")
        time.sleep(5)
        os.remove("sample.mp3")

    def test_invalid_language(self):
        # Test invalid language
        text = "Hello, how are you?"
        with self.assertRaises(ValueError):
            tts = gTTS(text=text, lang="invalid")

    def test_gtts_read_file(self):
        # Define test text to be used
        test_text = "Hello, world!"

        # Save test text to a file
        with open("test.txt", "w") as f:
            f.write(test_text)

        # Initialize gTTS object and read text from file
        with open("test.txt", "r") as f:
            text = f.read()
        tts = gTTS(text=text, lang="en")

        # Use gTTS to generate speech from text in file
        tts.save("test.mp3")
        assert os.path.exists("test.mp3")
        os.system("test.mp3")
        time.sleep(5)

        # Clean up test files
        os.remove("test.txt")
        os.remove("test.mp3")

    def test_noise_vs_text(self):
        # Test that speechrecognition can differentiate noise from text
        r = sr.Recognizer()
        
        # Load an audio file containing both noise and speech
        with sr.AudioFile("speech.wav") as source:
            audio = r.record(source)  # read the entire audio file
        
        # Test that speechrecognition can correctly identify noise and ignore it
        self.assertEqual(r.recognize_google(audio, show_all=True)["noise"], None)
        
        # Test that speechrecognition can correctly identify actual text in the audio file
        self.assertIn("Clapping sound", r.recognize_google(audio))

if __name__ == '__main__':
    unittest.main()