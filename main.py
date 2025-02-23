from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

service = Service(executable_path="chromedriver.exe") # chromedriver.exe downloaded from https://sites.google.com/chromium.org/driver/
driver = webdriver.Chrome(service=service)

# driver.current_window_handle

driver.get("http://localhost:8000")

time.sleep(1)

# Open the page with Selenium test elements
link_to_test_page = driver.find_element(By.LINK_TEXT, "Selenium Test Page").click()

# Click the button elements
# st_red_button = driver.find_element(By.CLASS_NAME, "")
# st_red_button.click()

# time.sleep(2)

# st_green_button = driver.find_element(By.CLASS_NAME, "")
# st_green_button.click()

# time.sleep(1)

# st_blue_button = driver.find_element(By.CLASS_NAME, "")
# st_blue_button.click()

time.sleep(1)

# Type something into a search bar
st_search_bar = driver.find_element(By.ID, "st-sb0").send_keys("Hello, World!")
time.sleep(1)

# Click through the radio buttons
st_radio_button0 = driver.find_element(By.ID, "st-rb1").click()
time.sleep(1)

st_radio_button1 = driver.find_element(By.ID, "st-rb0").click()
time.sleep(1)

st_radio_button2 = driver.find_element(By.ID, "st-rb2").click()
time.sleep(1)

# Go through all of the options on a select list
st_select_list = driver.find_element(By.ID, "st-sl0")
select_element_sl0 = Select(st_select_list)

select_element_sl0.select_by_value('option1')
time.sleep(1)

select_element_sl0.select_by_value('option2')
time.sleep(1)

select_element_sl0.select_by_value('option3')
time.sleep(1)

select_element_sl0.select_by_value('option4')
time.sleep(1)

# Possible to do with a loop?

# Go back to the main page
link_to_main_page = driver.find_element(By.LINK_TEXT, "AZ Main Page").click()

time.sleep(1)

driver.quit()