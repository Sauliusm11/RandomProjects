import pandas as pd
from itertools import permutations
import tkinter
import time
import pyautogui
import time
import ctypes
import tkinter

# Define constants for the keyboard events
# See https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes for a list of key codes
VK_CAPITAL = 0x14
VK_CONTROL = 0x11
VK_RETURN =	0x0D
A_KEY = 0x41
C_KEY = 0x43
V_KEY = 0x56
def get_values(Values):
    time.sleep(5)
    for i in range(0,5):
        pyautogui.moveTo(1800,500+(int(i)*100))
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        time.sleep(0.5)
        for j in range(0,12):
            pyautogui.moveTo(690+(j%4*150),570+(int(j/4)*150))
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            ctypes.windll.user32.keybd_event(VK_CONTROL, 0, 0, 0)  # Press the Control key
            ctypes.windll.user32.keybd_event(A_KEY, 0, 0, 0)  # Press the A key
            ctypes.windll.user32.keybd_event(A_KEY, 0, 2, 0)  # Release the A key
            ctypes.windll.user32.keybd_event(C_KEY, 0, 0, 0)  # Press the C key
            ctypes.windll.user32.keybd_event(C_KEY, 0, 2, 0)  # Release the C key
            ctypes.windll.user32.keybd_event(VK_CONTROL, 0, 2, 0)  # Release the Control key
            r = tkinter.Tk()
            item = r.clipboard_get()
            r.destroy()
            item = item[item.find("Penalty"):]
            item = item[item.find("\n"):]
            num1 = float(item[0:item.find("%")])
            item = item[item.find("/")+2:]
            num2 = float(item[0:item.find("%")])
            value = num1/100*5+num2/100*2+(100-num1-num2)/100*-2
            Values[i][j] = value
            print(value)
            time.sleep(0.4)
    return Values
    
def find_best_team_assignment(roles):
    current = [0,0,0,0,0]
    best = [0,0,0,0,0]
    curr_indexes = [0,0,0,0,0]
    best_indexes = [0,0,0,0,0]
    sum = 0
    best_sum = 0
    for i in range(0,12):
        if roles[0][i] > 0:
            current[0] = roles[0][i]
            curr_indexes[0] = i
            for j in  range(0,12):
                if roles[1][j] > 0 and j != i:
                    current[1] = roles[1][j]
                    curr_indexes[1] = j
                    for k in range(0,12):
                        if roles[2][k] > 0 and k != i and k != j:
                            current[2] = roles[2][k]
                            curr_indexes[2] = k
                            for l in range(0,12):
                                if roles[3][l] > 0 and l != i and l != j and l != k:
                                    current[3] = roles[3][l]
                                    curr_indexes[3] = l
                                    for h in range(0,12):
                                        if roles[4][h] > 0 and h != i and h != j and h != k and h != l:
                                            current[4] = roles[4][h]
                                            curr_indexes[4] = h
                                            sum = 0
                                            for s in range(0,5):
                                                sum+= current[s]
                                            if best_sum< sum:
                                                best = current.copy()
                                                best_indexes = curr_indexes.copy()
                                                best_sum = sum
    return best, best_sum, best_indexes
                            
Values = [[0 for x in range(12)] for y in range(5)]
roles = get_values(Values)
best_assignment, best_score, best_indexes = find_best_team_assignment(roles)

print("Best Team Assignment:", best_assignment)
print("Best Team Score:", best_score)
print("Best role indedexes(starting at 0):",best_indexes)
#Keeping the console open
while True:
    time.sleep(300)