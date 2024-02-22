from pyautogui import *
import webbrowser
import time
import threading
import keyboard

def check_end():
    if keyboard.is_pressed("End"):
        exit()
    time.sleep(0.1)
    check_end()
continue_thread = threading.Thread(target=check_end)
continue_thread.start()

print("At anytime you can press \"End\" to stop the program, please do not use to post negative comments")
link = input("What YouTube video do you want to comment on? (URL)\n")
comment = input("What do you want to comment?\n")
repeat = int(input("How many times do you want to post the comment? (Set to -1 for infinite)\n"))
account_for_delay = float(input("How much do you want to account for delay?\n"))

dev = False
if comment == "dev":
    dev = True
    link = r"https://www.youtube.com/watch?v=407SGZwLFlM&ab_channel=AbnormalNormality"
    repeat = 3
    account_for_delay = 2

x = 1
while not x - 1 == repeat:
    webbrowser.open(link)
    time.sleep(2.5 * account_for_delay)
    press("k")
    time.sleep(2.5 * account_for_delay)
    press("tab",24,0.3 * account_for_delay)
    if dev:
        comment = "This is comment {} from Python".format(x)
    typewrite(comment)
    press("tab",3,0.3 * account_for_delay)
    press("enter")
    press("f5")
    x += 1
    time.sleep(0.3 * account_for_delay)
    shortcut("ctrl","w")
    time.sleep(0.3 * account_for_delay)

shortcut("alt","tab")
press("end")