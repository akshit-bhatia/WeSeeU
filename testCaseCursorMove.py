import pyautogui
import unittest

class TestPyAutoGUI(unittest.TestCase):

    def test_move_to(self):
        # Move the mouse to position (100, 100)
        pyautogui.moveTo(100, 100)
        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Check that the mouse position is (100, 100)
        self.assertEqual((x, y), (100, 100))

    # hello world

    def test_navigate_to_word(self):
        # Locate an image of the word "hello world" on the screen and Get the center coordinates of the image
        center_x, center_y = pyautogui.locateCenterOnScreen('.\Testcases\\test3.jpg', confidence = 0.8)
        # Move the mouse to the center coordinates of the image
        pyautogui.moveTo(center_x, center_y)
        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Check that the mouse position is the same as the center coordinates of the image
        self.assertEqual((x, y), (center_x, center_y))

if __name__ == "__main__":
    unittest.main()