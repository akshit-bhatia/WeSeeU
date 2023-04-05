import pyautogui
import unittest
from gtts import gTTS
import os
import time
from PIL import Image
import math

class TestPyAutoGUI(unittest.TestCase):
    
    def setUp(self):
        # Set up gTTS language and voice
        self.language = 'en'
        self.voice = 'com.apple.speech.synthesis.voice.samantha'
        pyautogui.FAILSAFE = False
        
    def test_move_cursor_left(self):
        # Test moving cursor to the left by 100 pixels
        cursor_position = pyautogui.position()
        pyautogui.move(-100, 0, duration=0.25)
        new_position = pyautogui.position()
        self.assertEqual(new_position[0], cursor_position[0]-100)
        self.assertEqual(new_position[1], cursor_position[1])
        
        # Narrate the movement
        text = "Moving cursor to the left by 100 pixels"
        audio = gTTS(text=text, lang=self.language, tld='com', slow=False, lang_check=False)
        audio.save('audio.mp3')
        os.system("audio.mp3")
        time.sleep(5)
        
    def test_move_cursor_right(self):
        # Test moving cursor to the right by 100 pixels
        cursor_position = pyautogui.position()
        pyautogui.move(100, 0, duration=0.25)
        new_position = pyautogui.position()
        self.assertEqual(new_position[0], cursor_position[0]+100)
        self.assertEqual(new_position[1], cursor_position[1])
        
        # Narrate the movement
        text = "Moving cursor to the right by 100 pixels"
        audio = gTTS(text=text, lang=self.language, tld='com', slow=False, lang_check=False)
        audio.save('audio.mp3')
        os.system("audio.mp3")
        time.sleep(5)
    
    def test_move_cursor_up(self):
        # Test moving cursor up by 100 pixels
        cursor_position = pyautogui.position()
        pyautogui.move(0, -100, duration=0.25)
        new_position = pyautogui.position()
        self.assertEqual(new_position[0], cursor_position[0])
        self.assertEqual(new_position[1], cursor_position[1]-100)
        
        # Narrate the movement
        text = "Moving cursor up by 100 pixels"
        audio = gTTS(text=text, lang=self.language, tld='com', slow=False, lang_check=False)
        audio.save('audio.mp3')
        os.system("audio.mp3")
        time.sleep(5)
        os.remove("audio.mp3")
    
    def test_move_cursor_down(self):
        # Test moving cursor down by 100 pixels
        cursor_position = pyautogui.position()
        pyautogui.move(0, 100, duration=0.25)
        new_position = pyautogui.position()
        self.assertEqual(new_position[0], cursor_position[0])
        self.assertEqual(new_position[1], cursor_position[1]+100)
        
        # Narrate the movement
        text = "Moving cursor down by 100 pixels"
        audio = gTTS(text=text, lang=self.language, tld='com', slow=False, lang_check=False)
        audio.save('audio.mp3')
        os.system("audio.mp3")
        time.sleep(5)
        os.remove("audio.mp3")

    def test_movement_narate(self):
        img = Image.open(".\Testcases\\image.png")
        img.show()
        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Locate an image of the word "hello world" on the screen and Get the center coordinates of the image
        center_x, center_y = pyautogui.locateCenterOnScreen('.\Testcases\\image3.jpg', confidence = 0.8)
        
        # Calculate the angle between the two points
        angle = math.atan2(center_y - y, center_x - x)
        # Convert the angle to degrees
        angle = math.degrees(angle)
        # Convert negative angles to positive angles
        if angle < 0:
            angle += 360

        # Define the directional ranges in degrees
        directions = {
            'north': (337.5, 22.5),
            'northeast': (22.5, 67.5),
            'east': (67.5, 112.5),
            'southeast': (112.5, 157.5),
            'south': (157.5, 202.5),
            'southwest': (202.5, 247.5),
            'west': (247.5, 292.5),
            'northwest': (292.5, 337.5)
        }

        # Find the direction that corresponds to the angle
        for direction, (min_angle, max_angle) in directions.items():
            if angle >= min_angle and angle < max_angle:
                print(direction)

        # Move the mouse to the center coordinates of the image
        pyautogui.moveTo(center_x, center_y)

        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Check that the mouse position is the same as the center coordinates of the image
        self.assertEqual((x, y), (center_x, center_y))

if __name__ == '__main__':
    unittest.main()