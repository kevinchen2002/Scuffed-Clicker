import pyautogui
import datetime
import time

mouseSpeed = 0.5
timeOut = 10


def moveClick(xPos, yPos):
    pyautogui.moveTo(xPos, yPos, duration=mouseSpeed)
    pyautogui.click()


def imageClick(fileName):
    startTime = time.time()
    while True:
        currentTime = time.time()
        timePassed = currentTime - startTime
        if (timePassed > timeOut):
            print("Timeout: Image not found")
            return
        try:
            pyautogui.click(fileName, duration=mouseSpeed)
            break
        except:
            continue


def move(xPos, yPos):
    pyautogui.moveTo(xPos, yPos, duration=mouseSpeed)


def write(string):
    pyautogui.write(string)


def typeKey(string):
    if string == 'enter':
        pyautogui.write(['enter'])
    if string == 'backspace':
        pyautogui.write(['backspace'])
    else:
        pyautogui.write([string])


def scrollUp(units):
    pyautogui.scroll(units)


def scrollDown(units):
    pyautogui.scroll(-units)


def delay(delaySeconds):
    sleep(delaySeconds)


def waitUntil(targetTime):

    while True:
        currentTime = time.time()
        if (targetTime > currentTime):
            sleep(1)
            print(currentTime)
        else:
            continue


# imageClick("chrome.png")
# enterKeyboard("youtube.com")
# enterKeyboard(['enter'])
# imageClick("chrome.png")
# enterKeyboard(0, 0, "youtube.com")
# imageClick("youtube.png")
