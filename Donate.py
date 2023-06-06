#Importser
import pyautogui
import time
import subprocess
import keyboard

#Setting up variables
Goblins = pyautogui.locateCenterOnScreen("Resources/RequestGobs.png", confidence=0.9)
Wallbreakers = pyautogui.locateCenterOnScreen("Resources/RequestWbs.png", confidence=0.9)
Both = pyautogui.locateCenterOnScreen("Resources/RequestBoth.png", confidence=0.9)

Donate = pyautogui.locateCenterOnScreen("Resources/Donate.png", confidence=0.9)
Chat = pyautogui.locateCenterOnScreen("Resources/Chat.png", confidence=0.6)
ExitChat = keyboard.press_and_release('e')
ExitTrain = keyboard.press_and_release('r')

GoblinRefill = pyautogui.locateCenterOnScreen("Resources/GoblinRefill.png", confidence=0.9)
WallbreakerRefill = pyautogui.locateCenterOnScreen("Resources/WallbreakerRefill.png", confidence=0.9)
GoblinDonate = pyautogui.locateCenterOnScreen("Resources/GoblinDonate.png", confidence=0.7)
WallbreakerDonate = pyautogui.locateCenterOnScreen("Resources/WallbreakerDonate.png", confidence=0.7)

Train = pyautogui.locateCenterOnScreen("Resources/Train.png", confidence=0.9)
TrainTroops = pyautogui.locateCenterOnScreen("Resources/TrainTroops.png", confidence=0.9)

#Start Bluestacks
subprocess.Popen("C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe")
time.sleep(25)

#Open chat
pyautogui.moveTo(Chat, duration=0.1)
pyautogui.leftClick()
time.sleep(1)

#Start loop
i = 1
while 1 < 14401:

    #Look for Both Goblins and Wallbreakers
    if Both==None:
        pass
    else:
        pyautogui.moveTo(Donate, duration=0.1)
        pyautogui.leftClick()

        pyautogui.moveTo(WallbreakerDonate, duration=0.1)
        x = 0
        while x < 5:
            pyautogui.leftClick()
            x += 1
        
        pyautogui.moveTo(GoblinDonate, duration=0.1)
        x = 0
        while x < 4:
            pyautogui.leftClick()
            x += 1
        
        ExitChat
        time.sleep(2)

        pyautogui.moveTo(Train, duration=0.1)
        pyautogui.leftClick()

        pyautogui.moveTo(TrainTroops, duration=0.1)
        pyautogui.leftClick()

        pyautogui.moveTo(WallbreakerRefill, duration=0.1)
        x = 0
        while x < 5:
            pyautogui.leftClick()
            x += 1
        
        pyautogui.moveTo(GoblinRefill, duration=0.1)
        x = 0
        while x < 4:
            pyautogui.leftClick()
            x += 1
        
        ExitTrain
        time.sleep(2)

        pyautogui.moveTo(Chat, duration=0.1)
        pyautogui.leftClick()

    #Look for a Goblin request
    if Goblins==None:
        pass
    else:
        pyautogui.moveTo(Donate, duration=0.1)
        pyautogui.leftClick()

        pyautogui.moveTo(GoblinDonate, duration=0.1)
        x = 0
        while x < 4:
            pyautogui.leftClick()
            x += 1
        
        ExitChat
        time.sleep(2)

        pyautogui.moveTo(Train, duration=0.1)
        pyautogui.leftClick()

        pyautogui.moveTo(TrainTroops, duration=0.1)
        pyautogui.leftClick()

        pyautogui.moveTo(GoblinRefill, duration=0.1)
        x = 1
        while x < 4:
            pyautogui.leftClick()
            x += 1

        ExitTrain
        time.sleep(2)

        pyautogui.moveTo(Chat, duration=0.1)
        pyautogui.leftClick()
    
    #Look for a Wallbreaker request
    if Wallbreakers==None:
        pass
    else:
        pyautogui.moveTo(Donate, duration=0.1)
        pyautogui.leftClick()

        pyautogui.moveTo(WallbreakerDonate, duration=0.1)
        x = 0
        while x < 5:
            pyautogui.leftClick()
            x += 1
        
        ExitChat
        time.sleep(2)

        pyautogui.moveTo(Train, duration=0.1)
        pyautogui.leftClick()

        pyautogui.moveTo(TrainTroops, duration=0.1)
        pyautogui.leftClick()

        pyautogui.moveTo(WallbreakerRefill, duration=0.1)
        x = 0
        while x < 5:
            pyautogui.leftClick()
            x += 1
        
        ExitTrain
        time.sleep(2)

        pyautogui.moveTo(Chat, duration=0.1)
        pyautogui.leftClick()

    print("One iteration has passed")
    time.sleep(15)
    i += 1