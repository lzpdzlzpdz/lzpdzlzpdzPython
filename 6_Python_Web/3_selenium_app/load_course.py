#=coding:utf-8
"""
function:
    login page by python
author:
    lzpdzlzpdz
"""

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

def load_page(url):
    print "load page: %s" %(url)
    browser.get(url)
    

    time.sleep(1) 
    browser.find_element_by_id("username").send_keys('014206')
    browser.find_element_by_id("password").send_keys('014206')
    browser.find_element_by_id("password").send_keys(Keys.ENTER)
    
    
    time.sleep(5)
#     browser.quit()

def read_course(url):
    print "read_course: %s" %(url)
    browser.get(url)
    
    
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="li503"]/a').click()
    
    # 必读资料
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="t372"]/div[1]').click()

    time.sleep(6)
    browser.find_element_by_xpath('//*[@id="2991"]/span').click()


if __name__ == "__main__":
    print 'Doing...'
    
    load_page('http://222.73.244.148/portal/frk/trainingPlanStudent_study.action?planId=124&startLearn=false')
    
    read_course('http://222.73.244.148/portal/frk/trainingPlanStudent_study.action?planId=124&startLearn=false')
    
    print 'Done!'
    
    
    
