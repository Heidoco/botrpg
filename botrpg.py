import keyboard, pyautogui, time, schedule
from PySimpleGUI import PySimpleGUI as sg

def check():
    
    while pyautogui.locateOnScreen("Capturar.png"):
            playsound("a.mp3")

def hunt():
    keyboard.write('rpg hunt t')
    keyboard.press("enter")
    check()

def adv():
    keyboard.write('rpg adventure')
    keyboard.press("enter")
    check()
    
def heal():
    keyboard.write('rpg heal')
    keyboard.press("enter")
    check()
    
def raid():
    keyboard.write('rpg guild raid')
    keyboard.press("enter")
    check()

def upgrade():
    keyboard.write('rpg guild upgrade')
    keyboard.press("enter")
    check()
    
def pet_claim():
    keyboard.write('rpg pet adv claim a')
    keyboard.press("enter")
    check()

def pet_adv():
    keyboard.write('rpg pet adv learn a')
    keyboard.press("enter")
    check()

#INTERFACE
#LAYOUT
sg.theme("Reddit")
layout = [
    [sg.Text("Hunt")],
    [sg.Radio("Sim", "hunt", True),sg.Radio("Não", "hunt")],
    [sg.Text("Heal")],
    [sg.Radio("Sim", "Heal", True),sg.Radio("Não", "Heal")],
    [sg.Text("Adv")],
    [sg.Radio("Sim", "Adv", True),sg.Radio("Não", "Adv")],
    [sg.Text("Raid")],
    [sg.Radio("Sim","Raid",True),sg.Radio("Não","Raid")],
    [sg.Text("Pets")],
    [sg.Radio("Sim","Pets",True),sg.Radio("Não","Pets")],
    [sg.Button("Entrar")]
]
#JANELA
janela = sg.Window("Teste", layout)
#EVENTOS
while True:
    eventos, valores = janela.read()
    
    
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == "Entrar":
        if valores[0] == True:
            schedule.every(1).minutes.do(hunt)
        if valores[2] == True:
            schedule.every(3590).seconds.do(heal)
            schedule.every(58).seconds.do(heal)
        if valores[4] == True:
            schedule.every(1).hours.do(adv)
        if valores[6] == True:
            schedule.every(2).hours.do(raid)
        if valores[8] == True:
            schedule.every(240).minutes.do(pet_claim)
            schedule.every(241).minutes.do(pet_adv)
        time.sleep(5)
        schedule.run_all(delay_seconds=3)
        while True:
            schedule.run_pending()
            time.sleep(1)
            
            
            
            
#schedule.every(1).minutes.do(hunt)
#schedule.every(3590).seconds.do(heal)
#schedule.every(1).hours.do(adv)
#schedule.every(2).hours.do(raid)
#schedule.every(240).minutes.do(pet_claim)
#schedule.every(241).minutes.do(pet_adv)



