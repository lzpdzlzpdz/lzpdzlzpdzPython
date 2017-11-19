#=coding:utf-8
"""
function:
    login page by python
author:
    lzpdzlzpdz
"""

from selenium import webdriver
import time


browser = webdriver.Chrome()

def load_page(url):
    print "load page: %s" %(url)
    browser.get(url)
    
    time.sleep(1)
    browser.find_element_by_id("userbar-login").click()


    time.sleep(1) 
    browser.find_element_by_id("TANGRAM__PSP_10__userName").send_keys('lzpdzlzpdz@sina.cn')
    browser.find_element_by_id("TANGRAM__PSP_10__password").send_keys('139zhuyu')
    browser.find_element_by_id("TANGRAM__PSP_10__submit").submit()
    
    
    time.sleep(10)
#     browser.quit()

if __name__ == "__main__":
    print 'Doing...'
    
    load_page('https://zhidao.baidu.com/')
    
    print 'Done!'
    
    
    
