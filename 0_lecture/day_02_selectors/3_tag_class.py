import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://demo.nopcommerce.com/'

driver.get(url)

driver.maximize_window()

time.sleep(4)

# Scroll to the bottom of the page
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Give time for any dynamic content to load
time.sleep(3)

item_box = driver.find_elements(By.CLASS_NAME, 'item-box')
time.sleep(2)
print('the total item box== ',len(item_box))

time.sleep(10)