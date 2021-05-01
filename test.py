import pyautogui
dimensions = pyautogui.size()
print("width ", dimensions[0], " height ", dimensions[1])
pyautogui.moveTo(100, 100, duration=0.5)
pyautogui.moveTo(200, 100, duration=0.5)
pyautogui.moveTo(200, 200, duration=0.5)
pyautogui.moveTo(100, 200, duration=0.5)

print ("Hello this is Josh")

print("hello world")
image = pyautogui.locateOnScreen("1.PNG")
print(image)
pyautogui.moveTo(image[0]+(image[2]/2), image[1]+(image[3]/2), duration=0.5)
pyautogui.click()


# wait for image
# click image 
# click and type 
