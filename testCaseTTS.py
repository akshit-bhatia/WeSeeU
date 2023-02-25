import unittest
import pyttsx3

class TestTTSService(unittest.TestCase):
    def setUp(self):
        self.engine = pyttsx3.init()
    
    def test_tts_service(self):
        # Test the TTS service by providing a text input
        text = "Hello!"
        self.engine.say(text)
        self.engine.runAndWait()
        self.assertTrue(self.engine.isBusy(), "TTS service is running.")

    def test_tts_service2(self):
        self.engine = None
        try:
            self.engine.say("This is a test case when engine is not initialized")
            self.engine.runAndWait()
        except Exception as e:
            self.assertFalse(e, "Engine not initialized")

if __name__ == '__main__':
    unittest.main()