import pyautogui
import unittest
import time

class TestPyAutoGUI(unittest.TestCase):

    def test_move_to_default(self):
        pyautogui.FAILSAFE = False
        # Move the mouse to position (50, 50)
        pyautogui.moveTo(50, 50)

    def test_move_to_left(self):
        pyautogui.FAILSAFE = False
        # Move the mouse to position (50, 50)
        pyautogui.moveTo(50, 50)

        time.sleep(1)

        # Move the mouse to position (25, 50)
        pyautogui.moveTo(25, 50)

        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Check that the mouse position is (25, 50)
        self.assertEqual((x, y), (25, 50))

    def test_move_to_right(self):
        pyautogui.FAILSAFE = False
        # Move the mouse to position (50, 50)
        pyautogui.moveTo(50, 50)

        time.sleep(1)

        # Move the mouse to position (75, 50)
        pyautogui.moveTo(75, 50)

        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Check that the mouse position is (75, 50)
        self.assertEqual((x, y), (75, 50))

    def test_move_to_top(self):
        pyautogui.FAILSAFE = False
        # Move the mouse to position (50, 50)
        pyautogui.moveTo(50, 50)

        time.sleep(1)

        # Move the mouse to position (50, 25)
        pyautogui.moveTo(50, 25)

        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Check that the mouse position is (50, 25)
        self.assertEqual((x, y), (50, 25))

    def test_move_to_bottom(self):
        pyautogui.FAILSAFE = False
        # Move the mouse to position (50, 50)
        pyautogui.moveTo(50, 50)

        time.sleep(1)

        # Move the mouse to position (50, 75)
        pyautogui.moveTo(50, 75)

        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Check that the mouse position is (50, 75)
        self.assertEqual((x, y), (50, 75))

    def test_move_to_topLeft(self):
        pyautogui.FAILSAFE = False
        # Move the mouse to position (50, 50)
        pyautogui.moveTo(50, 50)

        time.sleep(1)

        # Move the mouse to position (25, 25)
        pyautogui.moveTo(25, 25)

        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Check that the mouse position is (25, 25)
        self.assertEqual((x, y), (25, 25))

    def test_move_to_topRight(self):
        pyautogui.FAILSAFE = False
        # Move the mouse to position (50, 50)
        pyautogui.moveTo(50, 50)

        time.sleep(1)

        # Move the mouse to position (75, 50)
        pyautogui.moveTo(75, 50)

        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Check that the mouse position is (75, 50)
        self.assertEqual((x, y), (75, 25))

    def test_move_to_bottomLeft(self):
        pyautogui.FAILSAFE = False
        # Move the mouse to position (50, 50)
        pyautogui.moveTo(50, 50)

        time.sleep(1)

        # Move the mouse to position (25, 75)
        pyautogui.moveTo(25, 75)

        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Check that the mouse position is (25, 75)
        self.assertEqual((x, y), (25, 75))

    def test_move_to_bottomRight(self):
        pyautogui.FAILSAFE = False
        # Move the mouse to position (50, 50)
        pyautogui.moveTo(50, 50)

        time.sleep(1)

        # Move the mouse to position (75, 75)
        pyautogui.moveTo(75, 75)

        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Check that the mouse position is (75, 75)
        self.assertEqual((x, y), (75, 75))

if __name__ == "__main__":
    unittest.main()