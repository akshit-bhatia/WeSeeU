import unittest
import speech_recognition as sr

class TestSpeechRecognition(unittest.TestCase):
    def setUp(self):
        self.recognizer = sr.Recognizer()
    
    def test_speech_recognition(self):
        self.audio_file = sr.AudioFile('.\Testcases\\test.wav')
        with self.audio_file as source:
            audio = self.recognizer.record(source)
        
        # Test the speech recognition by providing an audio file
        result = self.recognizer.recognize_google(audio)
        
        # Check if the result is not empty
        self.assertTrue(result, "Result from speech recognition is empty.")

    def test_speech_recognition1(self):
        self.audio_file = sr.AudioFile('.\Testcases\\test1.wav')
        with self.audio_file as source:
            audio = self.recognizer.record(source)
        
        # Test the speech recognition by providing an audio file
        result = self.recognizer.recognize_google(audio)
        
        # Check if the result is not empty
        self.assertTrue(result, "Result from speech recognition is empty.")

    def test_speech_recognition2(self):
        self.audio_file = sr.AudioFile('.\Testcases\\test2.wav')
        with self.audio_file as source:
            audio = self.recognizer.record(source)
        
        # Test the speech recognition by providing an audio file
        result = self.recognizer.recognize_google(audio)
        
        # Check if the result is not empty
        self.assertTrue(result, "Result from speech recognition is empty.")
        
    def tearDown(self):
        self.recognizer = None
        self.audio_file = None

if __name__ == '__main__':
    unittest.main()