from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="chromedriver.exe") # chromedriver.exe downloaded from https://sites.google.com/chromium.org/driver/
driver = webdriver.Chrome(service=service)

# driver.current_window_handle

driver.get("http://localhost:8000")

time.sleep(2)

# Open the page with Selenium test elements
link_to_test_page = driver.find_element(By.LINK_TEXT, "Selenium Test Page")
link_to_test_page.click()

# Click the button elements
# st_red_button = driver.find_element(By.CLASS_NAME, "button-red")
# st_red_button.click()

# time.sleep(2)

# st_green_button = driver.find_element(By.CLASS_NAME, "button-green")
# st_green_button.click()

# time.sleep(2)

# st_blue_button = driver.find_element(By.CLASS_NAME, "button-blue")
# st_blue_button.click()

# Go back to the main page
link_to_test_page = driver.find_element(By.LINK_TEXT, "AZ Main Page")
link_to_test_page.click()

time.sleep(10)

driver.quit()