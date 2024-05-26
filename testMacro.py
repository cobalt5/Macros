import time
import pyautogui as pyg
import pyperclip
pyg.PAUSE = 0.01
current = 1
time.sleep(2)
while True:
    typ = str(current)+' games ' + str(current*2) + 'mins, '
    pyperclip.copy(typ)
    pyg.keyDown('command')
    pyg.keyDown('v')
    pyg.keyUp('v')
    pyg.keyUp('command')
    pyg.keyDown('enter')
    pyg.keyUp('enter')
    current *= 2
    