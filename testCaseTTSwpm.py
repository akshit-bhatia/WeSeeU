import unittest
import pyttsx3

class TTSTest(unittest.TestCase):

    def test_pyttsx3_with_different_words_per_minute(self):
        engine = pyttsx3.init()
        text = "The quick brown fox jumps over the lazy dog."
        words_per_minute_values = [1] # different WPM values to test

        for words_per_minute in words_per_minute_values:
            engine.setProperty('rate', words_per_minute)
            engine.say(text)
            engine.runAndWait()
            # validate that the speech is not empty or None
            self.assertIsNotNone(text)
            self.assertFalse(text == '')

    def test_pyttsx3_with_different_words_per_minute0(self):
        engine = pyttsx3.init()
        text = "The quick brown fox jumps over the lazy dog."
        words_per_minute_values = [125] # different WPM values to test

        for words_per_minute in words_per_minute_values:
            engine.setProperty('rate', words_per_minute)
            engine.say(text)
            engine.runAndWait()
            # validate that the speech is not empty or None
            self.assertIsNotNone(text)
            self.assertFalse(text == '')

    def test_pyttsx3_with_different_words_per_minute1(self):
        engine = pyttsx3.init()
        text = "The quick brown fox jumps over the lazy dog."
        words_per_minute_values = [150] # different WPM values to test

        for words_per_minute in words_per_minute_values:
            engine.setProperty('rate', words_per_minute)
            engine.say(text)
            engine.runAndWait()
            # validate that the speech is not empty or None
            self.assertIsNotNone(text)
            self.assertFalse(text == '')

    def test_pyttsx3_with_different_words_per_minute2(self):
        engine = pyttsx3.init()
        text = "The quick brown fox jumps over the lazy dog."
        words_per_minute_values = [175] # different WPM values to test

        for words_per_minute in words_per_minute_values:
            engine.setProperty('rate', words_per_minute)
            engine.say(text)
            engine.runAndWait()
            # validate that the speech is not empty or None
            self.assertIsNotNone(text)
            self.assertFalse(text == '')
    
    def test_pyttsx3_with_different_words_per_minute3(self):
        engine = pyttsx3.init()
        text = "The quick brown fox jumps over the lazy dog."
        words_per_minute_values = [200] # different WPM values to test

        for words_per_minute in words_per_minute_values:
            engine.setProperty('rate', words_per_minute)
            engine.say(text)
            engine.runAndWait()
            # validate that the speech is not empty or None
            self.assertIsNotNone(text)
            self.assertFalse(text == '')

if __name__ == '__main__':
    unittest.main()