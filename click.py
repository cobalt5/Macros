from pynput import keyboard
import time
import random
import pyautogui
x = 0
def on_press(key):
    try:
        if key.char == ",":
            for i in range(20):
                pyautogui.click()
                time.sleep(random.uniform(0.001,0.005))
    except AttributeError:
        pass


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()