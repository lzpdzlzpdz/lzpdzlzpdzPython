#=coding:utf-8
"""
function:
    regex function
author:
    lzpdzlzpdz
"""

import pyautogui  
import time  
  

def draw_picture_by_mouse():
    
    try:
        time.sleep(5)  
        pyautogui.click()
        
        distance = 230  
        while distance > 0:  
            pyautogui.dragRel(distance, 0 ,duration = 0.2) #move right  
            distance = distance - 5  
            pyautogui.dragRel(0, distance, duration = 0.2) #move down  
            pyautogui.dragRel(-distance, 0, duration = 0.2) #move down  
            distance = distance - 5  
            pyautogui.dragRel(0 , -distance, duration = 0.2) #move up  
    except:
        print 'err'
  
if __name__ == "__main__":
    print "Doing..."
    
    draw_picture_by_mouse()
    
    print 'Done'
    
    
    