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
    browser.find_element_by_link_text("账户登录").click()


    time.sleep(1) 
    browser.find_element_by_id("loginname").send_keys('xxx')
    browser.find_element_by_id("nloginpwd").send_keys('xxx')
    browser.find_element_by_id("nloginpwd").send_keys(Keys.ENTER)
    
    time.sleep(5)
    
    browser.find_element_by_link_text("优惠券").click()
    
    time.sleep(1) 
    browser.find_element_by_xpath("//*[@id='quanlist']/div[10]/div[4]/div/a/span").click() 
    
    
#     browser.quit()

if __name__ == "__main__":
    print 'Doing...'
    
    load_page('https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F%3Fcu%3Dtrue%26utm_source%3Dbaidu-pinzhuan%26utm_medium%3Dcpc%26utm_campaign%3Dt_288551095_baidupinzhuan%26utm_term%3D0f3d30c8dba7459bb52f2eb5eba8ac7d_0_b85086c51c1840f38a32e0edf1cd52d8')
    
    print 'Done!'
    
    
    
