import pyautogui
import unittest
from PIL import Image
import time

class TestPyAutoGUI(unittest.TestCase):
        
    def test_navigate_to_1(self):
        img = Image.open(".\Testcases\\REQ002_img0.png")
        img.show()

        # Locate an enemy on the screen and Get the center coordinates of the image
        center_x, center_y = pyautogui.locateCenterOnScreen('.\Testcases\\REQ002_img0.png', confidence = 0.8)
        # Move the mouse to the center coordinates of the image
        pyautogui.moveTo(center_x, center_y)

        time.sleep(2)

        # Locate an image of the word "1" on the screen and Get the center coordinates of the image
        center_x, center_y = pyautogui.locateCenterOnScreen('.\Testcases\\REQ002_img1.png', confidence = 0.8)
        # Move the mouse to the center coordinates of the image
        pyautogui.moveTo(center_x, center_y)
        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Check that the mouse position is the same as the center coordinates of the image
        self.assertEqual((x, y), (center_x, center_y))

    def test_navigate_to_2(self):
        # Locate an enemy on the screen and Get the center coordinates of the image
        center_x, center_y = pyautogui.locateCenterOnScreen('.\Testcases\\REQ002_img0.png', confidence = 0.8)
        # Move the mouse to the center coordinates of the image
        pyautogui.moveTo(center_x, center_y)

        time.sleep(2)

        # Locate an image of the word "3" on the screen and Get the center coordinates of the image
        center_x, center_y = pyautogui.locateCenterOnScreen('.\Testcases\\REQ002_img2.png', confidence = 0.8)
        # Move the mouse to the center coordinates of the image
        pyautogui.moveTo(center_x, center_y)
        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Check that the mouse position is the same as the center coordinates of the image
        self.assertEqual((x, y), (center_x, center_y))

    def test_navigate_to_3(self):
        # Locate an enemy on the screen and Get the center coordinates of the image
        center_x, center_y = pyautogui.locateCenterOnScreen('.\Testcases\\REQ002_img0.png', confidence = 0.8)
        # Move the mouse to the center coordinates of the image
        pyautogui.moveTo(center_x, center_y)

        time.sleep(2)

        # Locate an image of the word "3" on the screen and Get the center coordinates of the image
        center_x, center_y = pyautogui.locateCenterOnScreen('.\Testcases\\REQ002_img3.png', confidence = 0.95)
        # Move the mouse to the center coordinates of the image
        pyautogui.moveTo(center_x, center_y)
        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Check that the mouse position is the same as the center coordinates of the image
        self.assertEqual((x, y), (center_x, center_y))
    
    def test_navigate_to_4(self):
        # Locate an enemy on the screen and Get the center coordinates of the image
        center_x, center_y = pyautogui.locateCenterOnScreen('.\Testcases\\REQ002_img0.png', confidence = 0.8)
        # Move the mouse to the center coordinates of the image
        pyautogui.moveTo(center_x, center_y)

        time.sleep(2)

        # Locate an image of the word "4" on the screen and Get the center coordinates of the image
        center_x, center_y = pyautogui.locateCenterOnScreen('.\Testcases\\REQ002_img4.png', confidence = 0.8)
        # Move the mouse to the center coordinates of the image
        pyautogui.moveTo(center_x, center_y)
        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Check that the mouse position is the same as the center coordinates of the image
        self.assertEqual((x, y), (center_x, center_y))

    def test_navigate_to_5(self):
        # Locate an enemy on the screen and Get the center coordinates of the image
        center_x, center_y = pyautogui.locateCenterOnScreen('.\Testcases\\REQ002_img0.png', confidence = 0.8)
        # Move the mouse to the center coordinates of the image
        pyautogui.moveTo(center_x, center_y)

        time.sleep(2)

        # Locate an image of the word "5" on the screen and Get the center coordinates of the image
        center_x, center_y = pyautogui.locateCenterOnScreen('.\Testcases\\REQ002_img5.png', confidence = 0.8)
        # Move the mouse to the center coordinates of the image
        pyautogui.moveTo(center_x, center_y)
        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Check that the mouse position is the same as the center coordinates of the image
        self.assertEqual((x, y), (center_x, center_y))

    def test_navigate_to_6(self):
        # Locate an enemy on the screen and Get the center coordinates of the image
        center_x, center_y = pyautogui.locateCenterOnScreen('.\Testcases\\REQ002_img0.png', confidence = 0.8)
        # Move the mouse to the center coordinates of the image
        pyautogui.moveTo(center_x, center_y)

        time.sleep(2)

        # Locate an image of the word "6" on the screen and Get the center coordinates of the image
        center_x, center_y = pyautogui.locateCenterOnScreen('.\Testcases\\REQ002_img6.png', confidence = 0.8)
        # Move the mouse to the center coordinates of the image
        pyautogui.moveTo(center_x, center_y)
        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Check that the mouse position is the same as the center coordinates of the image
        self.assertEqual((x, y), (center_x, center_y))

    def test_navigate_to_7(self):
        # Locate an enemy on the screen and Get the center coordinates of the image
        center_x, center_y = pyautogui.locateCenterOnScreen('.\Testcases\\REQ002_img0.png', confidence = 0.8)
        # Move the mouse to the center coordinates of the image
        pyautogui.moveTo(center_x, center_y)

        time.sleep(2)

        # Locate an image of the word "7" on the screen and Get the center coordinates of the image
        center_x, center_y = pyautogui.locateCenterOnScreen('.\Testcases\\REQ002_img7.png', confidence = 0.8)
        # Move the mouse to the center coordinates of the image
        pyautogui.moveTo(center_x, center_y)
        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Check that the mouse position is the same as the center coordinates of the image
        self.assertEqual((x, y), (center_x, center_y))

    def test_navigate_to_8(self):
        # Locate an enemy on the screen and Get the center coordinates of the image
        center_x, center_y = pyautogui.locateCenterOnScreen('.\Testcases\\REQ002_img0.png', confidence = 0.8)
        # Move the mouse to the center coordinates of the image
        pyautogui.moveTo(center_x, center_y)

        time.sleep(2)

        # Locate an image of the word "8" on the screen and Get the center coordinates of the image
        center_x, center_y = pyautogui.locateCenterOnScreen('.\Testcases\\REQ002_img8.png', confidence = 0.8)
        # Move the mouse to the center coordinates of the image
        pyautogui.moveTo(center_x, center_y)
        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Check that the mouse position is the same as the center coordinates of the image
        self.assertEqual((x, y), (center_x, center_y))

if __name__ == '__main__':
    unittest.main()