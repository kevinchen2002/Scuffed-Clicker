import pyautogui
dimensions = pyautogui.size()
print("width ", dimensions[0], " height ", dimensions[1])
pyautogui.moveTo(100, 100, duration=0.5)
pyautogui.moveTo(200, 100, duration=0.5)
pyautogui.moveTo(200, 200, duration=0.5)
pyautogui.moveTo(100, 200, duration=0.5)

print ("Hello this is Josh")

print("hello world")
image = pyautogui.locateOnScreen("Capture.PNG")
print(image)
pyautogui.moveTo(image[0], image[1], duration=0.5)
pyautogui.moveTo(image[0]+image[2], image[1], duration=0.5)
pyautogui.moveTo(image[0]+image[2], image[1]+image[3], duration=0.5)
pyautogui.moveTo(image[0], image[1]+image[3], duration=0.5)
pyautogui.moveTo(image[0], image[1], duration=0.5)