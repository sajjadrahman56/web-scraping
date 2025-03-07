import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://demo.nopcommerce.com/'

driver.get(url)

driver.maximize_window()

time.sleep(4)

driver.find_element(By.LINK_TEXT,"Register").click()
# driver.find_element(By.CLASS_NAME,'button-1').click()

time.sleep(10)