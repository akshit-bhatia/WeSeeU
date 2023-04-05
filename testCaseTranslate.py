import unittest
from googletrans import Translator

class TestGoogletrans(unittest.TestCase):
    
    def test_translation_eng_fr(self):
        translator = Translator()
        text = 'Hello World!'
        translated = translator.translate(text, dest='es')
        self.assertEqual(translated.text, '¡Hola Mundo!')

    def test_translation_fr_eng(self):
        translator = Translator()
        text = '¡Hola Mundo!'
        translated = translator.translate(text, dest='en')
        self.assertEqual(translated.text, 'Hello World!')
        
    def test_language_detection_fr(self):
        translator = Translator()
        text = 'Bonjour le monde!'
        detected = translator.detect(text)
        self.assertEqual(detected.lang, 'fr')

    def test_language_detection_hi(self):
        translator = Translator()
        text = 'Hello, nice to meet you!'
        detected = translator.detect(text)
        self.assertEqual(detected.lang, 'en')

if __name__ == '__main__':
    unittest.main()