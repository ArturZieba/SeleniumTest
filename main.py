from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="chromedriver.exe") # chromedriver.exe downloaded from https://sites.google.com/chromium.org/driver/
driver = webdriver.Chrome(service=service)

driver.current_window_handle

# driver.get("<webpage>")

# time.sleep(3)

# input_element_reject = driver.find_element(By.CLASS_NAME, "<class>")
# input_element_reject.send_keys(Keys.ENTER)

# input_element = driver.find_element(By.CLASS_NAME, "<class>")
# input_element.send_keys("test 123" + Keys.ENTER)

time.sleep(10)

driver.quit()