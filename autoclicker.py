import pyautogui
import keyboard
import time
pyautogui.PAUSE = 0.01
while 1:
    if keyboard.is_pressed('space'):
        time.sleep(1/20)
        while 1:
            if not keyboard.is_pressed('space'):
                pyautogui.click()
            else:
                break
        time.sleep(1/20)
print('no errors')
