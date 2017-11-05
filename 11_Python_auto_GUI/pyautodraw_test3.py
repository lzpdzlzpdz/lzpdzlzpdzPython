#=coding:utf-8
"""
function:
    regex function
author:
    lzpdzlzpdz
    
url:
    http://pyautogui.readthedocs.org/.
"""

import pyautogui  
import time  
  

def draw_picture_by_mouse():

    print 'sleep'
    time.sleep(5)
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.moveTo(100, 150)
    
    print 'click'
    pyautogui.click()
    pyautogui.moveRel(None, 10)  # move mouse 10 pixels down
    
    print 'doubleClick'
    pyautogui.doubleClick()
    pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.
    pyautogui.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
    
    print 'esc'
    pyautogui.press('esc')
    
    print 'shift'
    pyautogui.keyDown('shift')
    
    print 'left'
    pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
    
    print 'shift'
    pyautogui.keyUp('shift')
    pyautogui.hotkey('ctrl', 'c')

if __name__ == "__main__":
    print "Doing..."
    
    draw_picture_by_mouse()
    
    print 'Done'