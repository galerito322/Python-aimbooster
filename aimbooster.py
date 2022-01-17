from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

#encontra e seta a posição da janela do game dinamicamente toda vez que o bot é iniciado.
#sem essa verificação será necessário setar os valores da posição da janela manualmente toda vez que a mesma mudar de lugar.
a = None
while a is None:

    time.sleep(1)
    game_window = pyautogui.locateOnScreen('game_window.png', confidence = 0.8) #coordenadas da img

    if game_window != None:
        print("Image found", game_window)
        print("Game window position is now set !")
        a = input("Press enter to start the bot")    
    else:
        print("Retangle image not found yet")

#aimbot

print("The bot is runing ... can start the game\n Press (q) to exit !")

time.sleep(2)

def click(x,y):
    #semelhante ao pyautogui, porém muito mais rapido
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Color of center: (255, 219, 195)

while keyboard.is_pressed('q') == False:

    flag = 0
                            #x, y, width, height
    pic = pyautogui.screenshot(region=(game_window))
    #pic.save(r"./savedimage.png")
    width, height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):

            r, g, b = pic.getpixel((x, y))

            if  r == 255 and g == 219 and b == 195:
                flag = 1
                #  click(x + x, y + y)
                click(x + game_window.left, y + game_window.top)
                time.sleep(0.06)
                break

        if flag == 1:
            break
