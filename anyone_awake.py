import pyautogui
import time
pyautogui.PAUSE = 0.1

def typewords(word):
    for letter in word:
        pyautogui.keyDown(letter)
time.sleep(1800)
for i in range(9):
    
    typewords("anyone")
    pyautogui.press('space')
    typewords("awake?")
    pyautogui.keyUp('shift')
    pyautogui.keyDown('enter')
    time.sleep(1900)