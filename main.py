from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="chromedriver.exe") # chromedriver.exe downloaded from https://sites.google.com/chromium.org/driver/
driver = webdriver.Chrome(service=service)

driver.current_window_handle

time.sleep(10)

driver.quit()
