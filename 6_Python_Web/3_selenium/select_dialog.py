from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get('http://sahitest.com/demo/selectTest.htm')

s1 = Select(driver.find_element_by_id('s1Id'))
time.sleep(1)
print s1.select_by_index(1)
time.sleep(1)
print s1.select_by_value("o2")
time.sleep(1)
print s1.select_by_visible_text("o3")
time.sleep(1)
print s1.select_by_index(1)
time.sleep(1)
print s1.select_by_value("o2")
time.sleep(1)
print s1.select_by_visible_text("o3")
time.sleep(10)

driver.quit()