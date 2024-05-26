import pyautogui
import time
time.sleep(3)
x = 0
while True:
    l = []
    for c in str(x):
        l.append(c)
    for k in l:
        pyautogui.press(k)
    x+=1
    pyautogui.press('enter')
