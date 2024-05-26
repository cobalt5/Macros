
import pyautogui
import time
def shiftClick():
    pyautogui.keyDown('shift')
    pyautogui.click()
    pyautogui.keyUp('shift')
            

            
def cycles(length, yAddition):
    for x in range(length):
        pyautogui.moveTo(855+(36*x), 355+(36*yAddition))
        shiftClick()
        time.sleep(0.1)
        if (x % 2 != 0):
            anvil()
            time.sleep(0.3)


def working():
    pyautogui.click(855, 355)
    pyautogui.moveTo(856, 355)
    cycles(8, 0)
    time.sleep(0.5)
    cycles(8, 1)
    time.sleep(0.5)
    cycles(8, 0)
    time.sleep(0.5)
    cycles(4, 0)
    time.sleep(0.5)
    cycles(2, 0)


def cycles2(length, yAddition):
    pyautogui.click(855, 355)
    pyautogui.moveTo(856, 355)
    for x in range(length):
        pyautogui.moveTo(855+(36*x), 355+(36*yAddition))
        shiftClick()
        time.sleep(0.1)
        if (x % 2 != 0):
            anvil()
            time.sleep(0.3)

def anvil():
    time.sleep(0.1)
    pyautogui.moveTo(1000, 190)
    pyautogui.click()
    pyautogui.moveTo(1000, 154)
    shiftClick()

    
    

