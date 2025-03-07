import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://demo.nopcommerce.com/'

driver.get(url)

driver.maximize_window()

time.sleep(4)
driver.find_element(By.ID,'small-searchterms').send_keys('Apple iPhone 16 128GB')
time.sleep(5)
driver.find_element(By.CLASS_NAME,'button-1').click()

time.sleep(10)