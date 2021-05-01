import pyautogui
import datetime
import time

mouseSpeed = 0.5
timeOut = 5


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


def enterKeyboard(message):
    pyautogui.write(message)


# imageClick("chrome.png")
# enterKeyboard("youtube.com")
# enterKeyboard(['enter'])
# imageClick("chrome.png")
# enterKeyboard(0, 0, "youtube.com")
# imageClick("youtube.png")
