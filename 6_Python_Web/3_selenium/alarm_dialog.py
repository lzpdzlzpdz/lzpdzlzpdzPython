# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://sahitest.com/demo/alertTest.htm')

driver.find_element_by_name('b1').click()

a1 = driver.switch_to.alert  # 通过switch_to.alert切换到alert
sleep(1)
print a1.text  # text属性输出alert的文本
a1.accept()  # alert“确认”
sleep(10)

driver.quit()