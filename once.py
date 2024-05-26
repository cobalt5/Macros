import pyautogui
import time
pyautogui.PAUSE = 0.01
word = input('input the word')
letters = []
for char in word:
    letters.append(char)
time.sleep(2)
for n in letters:
    pyautogui.keyDown(n)
    pyautogui.keyUp(n)


