'''
    CSS SELECTORS
    1) TAG ID
    2) TAG CLASS
    3) TAG ATTRIBUTE
    4) TAG CLASS ATTRIBUTE
'''

import time
from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://tutorialsninja.com/demo/'

driver.get(url)

driver.maximize_window()

time.sleep(4)
#---------------------------- TAG CLASS [ SAME ID JUST USE # ]
# driver.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('Phone')
# driver.find_element(By.CSS_SELECTOR, '.form-control').send_keys('Phone')

#---------------------------- TAG ATTRIBUTE
driver.find_element(By.CSS_SELECTOR, 'input[name=search]').send_keys('Phone')
# --------------- OR
driver.find_element(By.CSS_SELECTOR, '[name=search]').send_keys('Phone')

time.sleep(3)
driver.quit()