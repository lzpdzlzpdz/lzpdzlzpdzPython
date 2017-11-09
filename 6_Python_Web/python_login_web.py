#=coding:utf-8
"""
function:
    send mail by python
author:
    lzpdzlzpdz
"""

from selenium import webdriver
import time


browser = webdriver.Chrome()

def load_page():
    print 'load_page'
    url= 'http://www.baidu.com'
    
    print "load page %s" %(url)
    browser.get(url)
    
    time.sleep(2)
    browser.find_element_by_id("kw").send_keys("python")
    browser.find_element_by_id("su").click()
    time.sleep(10)
    browser.quit()

if __name__ == "__main__":
    print 'Doing...'
    
    load_page()
    
    print 'Done!'
    
    
    
