from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from shutil import copyfileobj
import time
from urllib.request import urlopen

# Open Dev Tools
chrome_options = Options()
chrome_options.add_argument("--auto-open-devtools-for-tabs")

service = Service(executable_path="chromedriver.exe") # chromedriver.exe downloaded from https://sites.google.com/chromium.org/driver/
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the browser on http://localhost:8000
driver.get("http://localhost:8000")
time.sleep(1)

# Open the page with Selenium test elements
link_to_test_page = driver.find_element(By.LINK_TEXT, "Selenium Test Page").click()
time.sleep(3)

# Selenium Test Page code for checking here:

driver.execute_script("document.querySelector('#st-af0').play();")
time.sleep(0.5)
driver.execute_script("document.querySelector('#st-af0').volume = 0.5;")
time.sleep(0.5)
driver.execute_script("document.querySelector('#st-af0').pause();")
time.sleep(0.5)
driver.execute_script("document.querySelector('#st-af0').play();")
time.sleep(4)
driver.execute_script("document.querySelector('#st-af1').play();")
time.sleep(5)
driver.execute_script("document.querySelector('#st-af2').play();")
time.sleep(5)

# Add a test for lists
# Add a test for table
# Add a test for color picker
# Add some additional test for audio (ramping sound up/down with a loop?)

#####

# Click the button elements
st_red_button = driver.find_element(By.ID, "st-b0").click()
time.sleep(1)

st_green_button = driver.find_element(By.ID, "st-b1").click()
time.sleep(1)

st_blue_button = driver.find_element(By.ID, "st-b2").click()
time.sleep(1)

# Type something into a search bar
st_search_bar0 = driver.find_element(By.ID, "st-sb0")
st_search_bar0.send_keys("Hello, World!")
time.sleep(1)

# Copy contents of one search bar into another
st_search_bar0.send_keys(Keys.CONTROL, "a")
st_search_bar0.send_keys(Keys.CONTROL, Keys.SHIFT, "j")
time.sleep(1)
st_search_bar0.send_keys(Keys.CONTROL, "c")
time.sleep(1)

st_search_bar1 = driver.find_element(By.ID, "st-sb1")
st_search_bar1.send_keys(Keys.CONTROL, "v")
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

select_element_sl0_options = select_element_sl0.options

for option in select_element_sl0_options:
    select_element_sl0.select_by_value(option.get_attribute('value'))
    time.sleep(1)

# Enter log in information
st_login_username0 = driver.find_element(By.ID, "st-lf0-un0")
st_login_username0.send_keys("BobOfficial")
time.sleep(1)

st_login_password0 = driver.find_element(By.ID, "st-lf0-pw0")
st_login_password0.send_keys("Password123")
time.sleep(1)

st_login_submit_0 = driver.find_element(By.ID, "st-lf0-s0").click()
time.sleep(1)

# Download an image
st_image0_url = driver.find_element(By.ID, "st-img0").get_attribute("src")
time.sleep(1)

with urlopen(st_image0_url) as in_stream, open("downloaded_bober.png", "wb") as out_file:
    copyfileobj(in_stream, out_file)
time.sleep(1)

# Go back to the main page
link_to_main_page = driver.find_element(By.LINK_TEXT, "AZ Main Page").click()
time.sleep(1)

driver.quit()