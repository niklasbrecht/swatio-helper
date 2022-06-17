import cv2
import numpy as np
from PIL import ImageGrab
import time
import pyautogui



smallX = cv2.imread('./sources/smallX.png', cv2.IMREAD_GRAYSCALE)
delWarning = cv2.imread('./sources/deletionWarning.png', cv2.IMREAD_GRAYSCALE)


def getScreen():
    screenshot = np.array(ImageGrab.grab())
    convertScreenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    return convertScreenshot

def detectDelWarning():
    screen = getScreen()
    result = cv2.matchTemplate(screen, delWarning, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    threshold = .90
    if(max_val >= threshold):
        x = max_loc[0] * 0.5 + 50
        y = max_loc[1] * 0.5 + 30
        pyautogui.leftClick(x, y)
        return
    else:
        return

while True:    
    convertScreenshot = getScreen()
    result = cv2.matchTemplate(convertScreenshot, smallX, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    threshold = .90
    time.sleep(.3)
    if(max_val >= threshold):
        x = max_loc[0] * 0.5 + 15
        y = max_loc[1] * 0.5 + 10
        pyautogui.leftClick(x,y)
        time.sleep(.1)
        detectDelWarning()
