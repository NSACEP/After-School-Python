import pyautogui
from time import sleep

def moveMouse():
    for i in range(2):
        pyautogui.moveTo(100, 100, duration=0.25)
        pyautogui.moveTo(200, 100, duration=0.25)
        pyautogui.moveTo(200, 200, duration=0.25)
        pyautogui.moveTo(100, 200, duration=0.25)

def printCoordinates():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            pStr = f"x: {x}, y: {y}"
            print('\b' * len(pStr), end='', flush=True)
            # print(x,y)
    except KeyboardInterrupt:
        print('\nDone.')

def takeScreenShot():
    im = pyautogui.screenshot()

def isRed():
    pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))

def open_Ubuntu():
    l = list(pyautogui.locateOnScreen('images/ubuntu.png'))
    pyautogui.moveTo(l[0], l[1], duration=0.25)
    pyautogui.click(l[0], l[1])
    print(l)

def open_python3_console():
    l = list(pyautogui.locateOnScreen('images/ubuntu.png'))
    pyautogui.moveTo(l[0], l[1], duration=0.25)
    pyautogui.click(l[0], l[1])
    sleep(1)
    pyautogui.typewrite('python3')
    pyautogui.typewrite(["enter"])

def copy_all():
    pyautogui.click(*pyautogui.position())
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("a")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("a")

    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("c")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("c")


def cookie_clicker_bot():
    l = list(pyautogui.locateOnScreen('images/firefox.png'))
    pyautogui.moveTo(l[0], l[1], duration=0.25)
    pyautogui.click(l[0], l[1])
    sleep(1)

    delta = 20
    u = list(pyautogui.locateOnScreen('images/url.png'))
    pyautogui.moveTo(u[0], u[1], duration=0.25)
    pyautogui.click(u[0]+delta, u[1])
    pyautogui.typewrite('http://orteil.dashnet.org/cookieclicker/')
    pyautogui.typewrite(["enter"])

    m = list(pyautogui.locateOnScreen('images/maximize.png'))
    pyautogui.moveTo(m[0], m[1], duration=0.25)
    pyautogui.click(m[0] + delta, m[1]+ 10)
    sleep(5)

    # Resolution 1600x900
    deltax, deltay = 20, 20
    x,y = 1600/3/2, 900/2
    pyautogui.moveTo(x,y, duration=0.25)
    for k in range(101):
        pyautogui.click(x,y)


cookie_clicker_bot()