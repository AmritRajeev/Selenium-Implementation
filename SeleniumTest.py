from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import random as rd


alpha = 'a'
test_list=list()
for i in range(0, 26):
    test_list.append(alpha) 
    alpha = chr(ord(alpha) + 1)
    

r = rd.choice(test_list)
test = 'someword'+r  

email = test
url='https://login.yahoo.com/account/create?specId=yidReg'

driver= webdriver.Chrome(r'C:\Users\User\AppData\Local\Programs\Python\Python37\ChromeDriver\ChromeDriver.exe')
driver.get(url)
time.sleep(2)

driver.find_element_by_id("usernamereg-firstName").send_keys(test)
time.sleep(5)

driver.find_element_by_id("usernamereg-lastName").send_keys('girish')
time.sleep(5)
    
driver.find_element_by_id("usernamereg-yid").send_keys(email)
time.sleep(5)

driver.find_element_by_id("usernamereg-password").send_keys('nibbayousuck')
time.sleep(5)

driver.find_element_by_id("usernamereg-phone").send_keys('9448935365')
time.sleep(5)

driver.find_element_by_id("usernamereg-month").send_keys('august')
time.sleep(5)

driver.find_element_by_id("usernamereg-day").send_keys('03')
time.sleep(5)

driver.find_element_by_id("usernamereg-year").send_keys('2000')
time.sleep(5)
    
submitBtn=driver.find_element_by_id("reg-submit-button")
submitBtn.click()    
