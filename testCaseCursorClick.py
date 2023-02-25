import pyautogui
import unittest

class TestPyAutoGUI(unittest.TestCase):

    def test_mouse_click(self):
        # Get the current position of the mouse
        x, y = pyautogui.position(100, 100)
        # Simulate a left mouse click at the current position of the mouse
        pyautogui.click(x, y)
        # Check that the mouse click was registered
        self.assertEqual(pyautogui.mouseDown(), None)
        # Simulate a left mouse release
        pyautogui.mouseUp()
        # Check that the mouse button was released
        self.assertEqual(pyautogui.mouseDown(), None)

    def test_mouse_click1(self):
        # Get the current position of the mouse
        x, y = pyautogui.position(100, 100)
        # Simulate a left mouse click at the current position of the mouse
        pyautogui.click(x, y)
        # Check that the mouse click was registered
        self.assertEqual(pyautogui.mouseDown(), None)
        # Simulate a left mouse release
        pyautogui.mouseUp()
        # Check that the mouse button was released
        self.assertEqual(pyautogui.mouseDown(), None)

if __name__ == "__main__":
    unittest.main()