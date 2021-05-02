from pathlib import Path
import os
import re
import pyautogui
import datetime
import timehttps://www.google.com/recaptcha/api2/demo



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
    time.sleep(delaySeconds)


def waitUntil(targetTime):
    while True:
        currentTime = time.time()
        if (targetTime > currentTime):
            time.sleep(1)
            print(currentTime)
        else:
            continue


# read the file
def read_by_line(foldername):

    filename = foldername + ".txt"
    input_file = open(Path("./") / foldername / filename)
    lines = input_file.readlines()

    return lines

moveFind = re.compile(r"""move\s\((\d*),(\d*)\)""")
imageFind = re.compile(r"""imageclick\s\((.*?)\)""")
clickFind = re.compile(r"""click\s\((\d*),(\d*)\)""")   
writeFind = re.compile(r"""write\s\((.*?)\)""")
delayFind = re.compile(r"""delay\s\((\d*?)\)""")
scollDownFind = re.compile(r"""scrolldown\s\((\d*?)\)""")
scollUpFind = re.compile(r"""scrollup\s\((\d*?)\)""")
typeKeyFind = re.compile(r"""typekey\s\((.*?)\)""")


def are_commands_valid(list_of_lines):
    for line in list_of_lines:
        line.lower()
        if line.startswith("imageclick"):
            check = imageFind.search(line)
            if (check == None):
                return False
            else:
                continue

        elif line.startswith("move"):
            check = moveFind.search(line)
            if (check == None):
                return False
            else:
                continue

        elif line.startswith("clickfind"):
            check = clickFind.search(line)
            if (check == None):
                return False
            else:
                continue

        elif line.startswith("write"):
            check = writeFind.search(line)
            if (check == None):
                return False
            else:
                continue

        elif line.startswith("typekey"):
            check = typeKeyFind.search(line)
            if (check == None):
                return False
            else:
                continue

        elif line.startswith("scrollup"):
            check = typekeyFind.search(line)
            if (check == None):
                return False
            else:
                continue

        elif line.startswith("scrolldown"):
            check = scrolldownFind.search(line)
            if (check == None):
                return False
            else:
                continue

        elif line.startswith("delay"):
            check = delayFind.search(line)
            if (check == None):
                return False
            else:
                continue
    return True

# reads line and excutes appropiate command
def parse_line(line):

    command = line[0: 10].lower()
    if command == "imageclick":
        print(command)
        param = line.split(" ")[1]
        param = param[1:len(param)-2]
        param = str(Path("./images") / param)
        print(param)
        imageClick(param)

    command = line[0: 5].lower()
    if command == "click":
        print(command)
        params = line.split(" ")[1]
        first_param = params[1: len(params)-2].split(",")[0]
        second_param = params[1: len(params)-2].split(",")[1]
        print(first_param)
        print(second_param)
        moveClick(int(first_param), int(second_param))

    command = line[0: 4].lower()
    if command == "move":
        print(command)
        params = line.split(" ")[1]
        first_param = params[1: len(params)-1].split(",")[0]
        second_param = params[1: len(params)-2].split(",")[1]
        print(first_param)
        print(second_param)
        move(int(first_param), int(second_param))

    command = line[0: 5].lower()
    if command == "write":
        print(command)
        param = line.split(" ")[1]
        param = param[1: len(param)-2]
        write(param)

    command = line[0: 7].lower()
    if command == "typekey":
        print(command)
        param = line.split(" ")[1]
        param = param[1: len(param)-2]
        print(param)
        typeKey(param)

    command = line[0: 8].lower()
    if command == "scrollup":
        print(command)
        param = line.split(" ")[1]
        param = param[1: len(param)-2]
        scrollUp(int(param))

    command = line[0: 10].lower()
    if command == "scrolldown":
        print(command)
        param = line.split(" ")[1]
        param = param[1: len(param)-2]
        scrollDown(int(param))



    command = line[0: 5].lower()
    if command == "delay":
        print(command)
        param = line.split(" ")[1]

        param = param[1: len(param)-1]
        delay(param)


foldername = input("Please enter the folder to run (or q to quit): ")
while foldername != "q":   

    lines = read_by_line(foldername)
    if are_commands_valid(lines):
        for line in lines:
            time.sleep(0.5)
            parse_line(line)

foldername = input("Please enter the folder to run (or q to quit): ")

print("done")
