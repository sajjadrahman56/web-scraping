import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# service_obj = Service(r'C:\driver-tools\chromedriver.exe') geckodriver.exe edge msedgedriver.exe firefox

#   -------------------------------- if use Chrome ------------------
# service_chrome_driver = Service(r'C:\driver-tools\chromedriver.exe')
# driver = webdriver.Firefox(service=service_chrome_driver)

#   -------------------------------- if use FireFox ------------------
# service_firefox_driver = Service(r'C:\driver-tools\geckodriver.exe')
# driver = webdriver.Firefox(service=service_firefox_driver)

#   -------------------------------- if use Edge ------------------
service_edge_driver = Service(r'C:\driver-tools\msedgedriver.exe')
driver = webdriver.Edge(service=service_edge_driver)


url = 'https://opensource-demo.orangehrmlive.com/'

driver.get(url)

time.sleep(3)

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")

driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
# driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()
time.sleep(3)

actual_title = driver.title
exp_title = "OrangeHRM"

if actual_title == exp_title:
    print("Test Pass")

driver.quit()
