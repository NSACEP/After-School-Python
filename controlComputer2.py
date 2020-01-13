from pyautogui import *
from time import sleep, time

def timer(func):
    ti = time()
    func()
    tf = time()
    return tf - ti

# nsacep mail.com
def open_chrome():
    deltaX = -50
    l = list(locateOnScreen('PIC/chrome_icon.png'))
    click(l[0]+ deltaX, l[1])
    print(l)

open_chrome()