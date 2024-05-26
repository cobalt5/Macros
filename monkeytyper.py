import pyautogui
import time

text = input('what do you want to type')
pyautogui.PAUSE = 2.2250738585072014e-308
h = {
    'a':'a',
    'b':'b',
    'c':'c',
    'd':'d',
    'e':'e',
    'f':'f',
    'g':'g',
    'h':'h',
    'i':'i',
    'j':'j',
    'k':'k',
    'l':'l',
    'm':'m',
    'n':'n',
    'o':'o',
    'p':'p',
    'q':'q',
    'r':'r',
    's':'s',
    't':'t',
    'u':'u',
    'v':'v',
    'w':'w',
    'x':'x',
    'y':'y',
    'z':'z',
    ' ': "SPACE"
}
time.sleep(3)
for i in range(len(text)):
    pyautogui.keyDown(h[text[i]])
    pyautogui.keyUp(h[text[i]])
