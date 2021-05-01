import pyautogui
dimensions = pyautogui.size()
print("width ", dimensions[0], " height ", dimensions[1])
pyautogui.moveTo(100, 100, duration=0.5)
pyautogui.moveTo(200, 100, duration=0.5)
pyautogui.moveTo(200, 200, duration=0.5)
pyautogui.moveTo(100, 200, duration=0.5)
pyautogui.move(-100, 0, duration=0.5)

print ("Hello this is Josh")

print("hello world")
image = pyautogui.locateOnScreen("Capture.png")
print(image)
pyautogui.moveTo(image[0]+(image[2]/2), image[1]+(image[3]/2), duration=0.5)
#pyautogui.click()
pyautogui.click()

# pyautogui.click('Capture.png')
pyautogui.write(['backspace'])
pyautogui.write("google.ca")
pyautogui.write(['enter'])

#returns the current mouse position
#p = pyautogui.position()

#you can use pyautogui.click(10, 10, button='left')

