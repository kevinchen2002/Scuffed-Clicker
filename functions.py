import pyautogui
import datetime
import time

# mouseSpeed = 0.5
# timeOut = 5


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


def waitTime(targetTime):
    # todo: convert target time into something the program can use
    while True:
        currentTime = datetime.datetime.now()
        if (targetTime > currentTime):
            sleep(1)
        else:
            continue


def enterKeyboard(xPos, yPos, message):
    #pyautogui.moveTo(xPos, yPos)
    pyautogui.write(message)


# imageClick("chrome.png")
# enterKeyboard(0, 0, "youtube.com")
# imageClick("youtube.png")