import unittest
import speech_recognition as sr

class TestSpeechInput(unittest.TestCase):
    
    def test_speech_input(self):
        # Initialize recognizer
        r = sr.Recognizer()

        # Use microphone as source for audio input
        with sr.Microphone() as source:
            print("Speak something!")
            # Adjust for ambient noise
            r.adjust_for_ambient_noise(source)
            # Listen for audio input
            audio = r.listen(source)

        # Convert audio input to text
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            self.assertIsNotNone(text)
        except sr.UnknownValueError:
            print("Oops! Could not understand audio input.")
            self.fail("Speech input could not be understood.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            self.fail("Error with Google Speech Recognition service.")

if __name__ == '__main__':
    unittest.main()