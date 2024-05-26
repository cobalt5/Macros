import pyautogui
import time
pyautogui.PAUSE = 0.01
word = input('input the word')
time.sleep(2)
letters = []
for char in word:
    letters.append(char)
while True:
    for n in letters:
        pyautogui.keyDown(n)
        pyautogui.keyUp(n)
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
