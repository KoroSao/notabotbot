import pyautogui, time, wget
time.sleep(2)
coords = pyautogui.locateOnScreen('notabot.png', confidence=0.9 )
print(coords)
pyautogui.moveTo(coords.left + 30 , coords.top +30, 2, pyautogui.easeOutQuad)
time.sleep(0.8)
pyautogui.leftClick()


