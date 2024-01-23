import pyautogui
import time
import ctypes

# Define constants for the keyboard events
# See https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes for a list of key codes
# VK_MENU = 0x12  # Alt key code
# VK_LSHIFT = 0xA0  # Left shift key code
VK_CAPITAL = 0x14
moved = 0
while True:
    # Move the mouse slightly
    pyautogui.moveRel(10, 10)

    # Simulate a key press event to prevent the screen from turning off
    # ctypes.windll.user32.keybd_event(VK_MENU, 0, 0, 0)  # Press the Alt key
    # ctypes.windll.user32.keybd_event(VK_LSHIFT, 0, 0, 0)  # Press the left Shift key
    # ctypes.windll.user32.keybd_event(VK_LSHIFT, 0, 2, 0)  # Release the left Shift key
    # ctypes.windll.user32.keybd_event(VK_MENU, 0, 2, 0)  # Release the Alt key
    ctypes.windll.user32.keybd_event(VK_CAPITAL, 0, 0, 0)  # Release the left Shift key
    ctypes.windll.user32.keybd_event(VK_CAPITAL, 0, 2, 0)  # Release the Alt key
   
    print(moved)
    moved+=1
    # Wait for 5 minutes
    time.sleep(300)

