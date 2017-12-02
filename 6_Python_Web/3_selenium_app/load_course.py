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



def load_page(browser,url):

    
    print "load page: %s" %(url)
    browser.get(url)
    

    time.sleep(1) 
    browser.find_element_by_id("username").send_keys('014206')
    browser.find_element_by_id("password").send_keys('014206')
    browser.find_element_by_id("password").send_keys(Keys.ENTER)
    
    
    time.sleep(5)
#     browser.quit()

def read_course(browser,url,index):

    try:
        print "read_course: %s" %(url)
        browser.get(url)
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="li503"]/a').click()
        time.sleep(3)
        
        # 必读资料337----374
    
        print index
        str = '//*[@id="t%d"]/div[1]'%index
        print str
        browser.find_element_by_xpath(str).click()
        time.sleep(3)
    except:
        return
    
    for inloop in range(2000,6000):
        try:
            #1.判断是否读过
            statusstr = '//*[@id="rid%d"]/td[7]/div/span'%inloop
            print statusstr
            result =  browser.find_element_by_xpath(statusstr).text
            print result
            if '已完成' in result:
                print 'already read...'
                continue 
            
            #2.阅读未读的
            #print inloop
            instr = '//*[@id="%d"]/span'%inloop
            print instr
            browser.find_element_by_xpath(instr).click()
            print 'success'
            time.sleep(10)
            return
        except:
            pass


if __name__ == "__main__":
    print 'Doing...'
    
    for index in range(326,388):
        browser = webdriver.Chrome()
        browser.maximize_window()
        
        url = 'http://222.73.244.148/portal/frk/trainingPlanStudent_study.action?planId=124&startLearn=false'
        
        
        load_page(browser,url)
    
        read_course(browser,url,index)
    
    
    print 'Done!'
    
    
    
