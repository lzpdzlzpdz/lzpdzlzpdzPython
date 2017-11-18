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
    
    '''
    <input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
    '''
    
    #1. clear
    browser.find_element_by_id("kw").clear()
    #2. send_keys
    browser.find_element_by_id("kw").send_keys("python")

    #4.
    ret = browser.find_element_by_id("su").get_attribute("autocomplete")
    print ret
    #5.
    ret = browser.find_element_by_id("su").location
    print ret
    #6.
    ret = browser.find_element_by_id("su").text
    print ret
    #7.
    ret = browser.find_element_by_id("su").__str__()
    print ret

    #8.
    ret = browser.find_element_by_id("su")._parent
    print ret

    #3. click
    browser.find_element_by_id("su").click()
    
    
    time.sleep(10)
    browser.quit()

if __name__ == "__main__":
    print 'Doing...'
    
    load_page()
    
    print 'Done!'
    
    
    
