import keyboard, pyautogui, time
#time.sleep(5)

pyautogui.click(410,816)
def check():
    while pyautogui.locateOnScreen("checkcoin.png"):
            keyboard.write('fish')
            keyboard.press("enter")
            time.sleep(1)
    while pyautogui.locateOnScreen("jailcheck.png"):
        keyboard.write('rpg jail')
        keyboard.press("enter")
        time.sleep(1)
        keyboard.write("protest")
        keyboard.press("enter")
        time.sleep(1)
        if pyautogui.locateOnScreen("checkcoin.png", grayscale=True):
            keyboard.write('fish')
            keyboard.press("enter")
            time.sleep(1)


while True:
    for i in range(5):
        check()
        keyboard.write('rpg hunt')
        keyboard.press("enter")
        time.sleep(10)
        check()
        keyboard.write('rpg buy life potion')
        keyboard.press("enter")
        time.sleep(10)
        check()
        keyboard.write('rpg heal')
        keyboard.press("enter")
        time.sleep(10)
        check()
        time.sleep(32)
        check()


    '''
    keyboard.write('rpg buy life potion')
    keyboard.press("enter")
    check()

    keyboard.write('rpg heal')
    keyboard.press("enter")
    check()
    '''
    
    keyboard.write('rpg fish')
    keyboard.press("enter")
    time.sleep(1)
    check()


