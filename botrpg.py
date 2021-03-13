import keyboard, pyautogui, time
from playsound import playsound
time.sleep(5)






def check():
    while pyautogui.locateOnScreen("Capturar.png", region=(310,120,650,620)):
            playsound("a.mp3")
"""
while True:
    keyboard.write('rpg craft epic log all')
    keyboard.press("enter")
    check()
    keyboard.write('rpg dismantle epic log all')
    keyboard.press("enter")
    check()
"""
while True:
    keyboard.write('rpg guild raid')
    keyboard.press("enter")
    check()
    for x in range(2):
        keyboard.write('rpg heal')
        keyboard.press("enter")
        time.sleep(2)
        keyboard.write('rpg adventure')
        keyboard.press("enter")
        check()
        time.sleep(2)
        #keyboard.write('rpg heal')
        #keyboard.press("enter")
        #time.sleep(2)
        for a in range(12):
            keyboard.write('rpg chainsaw')
            keyboard.press("enter")
            time.sleep(3)
            #keyboard.write('rpg heal')
            #keyboard.press("enter")
            check()
            for i in range(5):
                check()
                keyboard.write('rpg hunt t')
                keyboard.press("enter")
                check()
                #keyboard.write('rpg heal')
                #keyboard.press("enter")
                #check()
                time.sleep(20)
                time.sleep(39)