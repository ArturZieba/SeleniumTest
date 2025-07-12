# Module containing unit tests for the Selenium Test page
# Run all test cases: python stpunittests.py (where stpunittests.py is the name of the .py file that contains these unit tests)
# Run a specific test case: python stpunittests.py <unit test class>.<test case name> (for example: python stpunittests.py Tests.test_click_radio_buttons)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from shutil import copyfileobj
from support import FontModifiers
import time
import unittest
from urllib.request import urlopen

class Tests(unittest.TestCase):
    # Substitue explicit wait function for use instead of time.sleep()
    def wait_for_element(self, by, identifier, condition, timeout = 15):
        return WebDriverWait(self.driver, timeout).until(condition((by, identifier)))

    def setUp(self):
        try:
            FontModifiers.font_cyan(f"RUNNING UNIT TEST: {self._testMethodName}") # Rewrite?

            # Open Dev Tools
            chrome_options = Options()
            chrome_options.add_argument("--auto-open-devtools-for-tabs") # Potential chromedriver/chrome verisons mismatch, comment out for the time being

            service = Service(executable_path="chromedriver.exe") # chromedriver.exe downloaded from https://sites.google.com/chromium.org/driver/
            self.driver = webdriver.Chrome(service=service, options=chrome_options)

            self.driver.get("http://localhost:8000")

            # Open the page with Selenium test elements
            self.wait_for_element(By.LINK_TEXT, "Selenium Test Page", EC.element_to_be_clickable).click()
        except:
            assert False, FontModifiers.string_font_bold_red(f"{self._testMethodName}: setUp() function failed")  
    
    ##### 
    
    # setUp/tearDown desc?
    # Check "DevTools listening on" print in the Console
    # Log to a file?
    # Add a test for lists
    # Add a test for table
    # Add a test for color picker
    # Add some additional test for audio (ramping sound up/down with a loop?)
    
    #####
    
    # Click the button elements
    def test_click_buttons(self):
        try:
            self.wait_for_element(By.ID, "st-b0", EC.element_to_be_clickable).click()
    
            self.wait_for_element(By.ID, "st-b1", EC.element_to_be_clickable).click()
    
            self.wait_for_element(By.ID, "st-b2", EC.element_to_be_clickable).click()
        except:
            assert False, FontModifiers.string_font_bold_red(f"{self._testMethodName}: Clicking buttons failed")

    # Click through the radio buttons
    def test_click_radio_buttons(self):
        try:
            self.wait_for_element(By.ID, "st-rb1", EC.element_to_be_clickable).click()
        
            self.wait_for_element(By.ID, "st-rb0", EC.element_to_be_clickable).click()
        
            self.wait_for_element(By.ID, "st-rb2", EC.element_to_be_clickable).click()
        except:
            assert False, FontModifiers.string_font_bold_red(f"{self._testMethodName}: Clicking radio buttons failed")
    
    # Check color picker
    def test_color_picker(self):
        try:
            print("Hi")
        except:
            assert False, FontModifiers.string_font_bold_red(f"{self._testMethodName}: Using color picker failed")

    # Download an image
    def test_download_image(self):
        try:
            st_image0_url = self.wait_for_element(By.ID, "st-img0", EC.element_to_be_clickable).get_attribute("src")
        
            with urlopen(st_image0_url) as in_stream, open("downloaded_bober.png", "wb") as out_file:
                copyfileobj(in_stream, out_file)
        except:
            assert False, FontModifiers.string_font_bold_red(f"{self._testMethodName}: Downloading an image failed")

    # Play through different audio elements
    def test_play_audio_elements(self):
        try:
            # Better describe what does each part does
            self.driver.execute_script("document.querySelector('#st-af0').play();")
            time.sleep(0.5)
            
            self.driver.execute_script("document.querySelector('#st-af0').volume = 0.5;")
            time.sleep(0.5)
            
            self.driver.execute_script("document.querySelector('#st-af0').pause();")
            time.sleep(0.5)
            
            self.driver.execute_script("document.querySelector('#st-af0').play();")
            time.sleep(4)
            
            self.driver.execute_script("document.querySelector('#st-af1').play();")
            time.sleep(5)
            
            self.driver.execute_script("document.querySelector('#st-af2').play();")
            time.sleep(5)
        except:
            assert False, FontModifiers.string_font_bold_red(f"{self._testMethodName}: Playing audio elements failed")

    # Go through all of the options on a select list
    def test_select_list_select_all_options(self):
        try:
            st_select_list = self.wait_for_element(By.ID, "st-sl0", EC.element_to_be_clickable)
            select_element_sl0 = Select(st_select_list)
        
            select_element_sl0_options = select_element_sl0.options
        
            for option in select_element_sl0_options:
                select_element_sl0.select_by_value(option.get_attribute('value'))
        except:
            assert False, FontModifiers.string_font_bold_red(f"{self._testMethodName}: Selecting from a select list failed")

    # Go back to the main page
    def test_stp_to_main(self):
        try:
            self.wait_for_element(By.LINK_TEXT, "AZ Main Page", EC.element_to_be_clickable).click()
        except:
            assert False, FontModifiers.string_font_bold_red(f"{self._testMethodName}: Going back to main page failed")

    # Type and copy/paste something into a search bar
    def test_type_in_search_bar(self):
        try:
            st_search_bar0 = self.wait_for_element(By.ID, "st-sb0", EC.element_to_be_clickable)
            st_search_bar0.send_keys("Hello, World!")
        
            # Copy contents of one search bar into another
            st_search_bar0.send_keys(Keys.CONTROL, "a") # Select all
            st_search_bar0.send_keys(Keys.CONTROL, "c") # Copy
        
            st_search_bar1 = self.wait_for_element(By.ID, "st-sb1", EC.element_to_be_clickable)
            st_search_bar1.send_keys(Keys.CONTROL, "v") # Paste   
        except:
            assert False, FontModifiers.string_font_bold_red(f"{self._testMethodName}: Search Bar typing or copy/pasting failed")

    # Enter log in information
    def test_use_login(self):
        try:
            # Enter username
            st_login_username0 = self.wait_for_element(By.ID, "st-lf0-un0", EC.element_to_be_clickable)
            st_login_username0.send_keys("BobOfficial")

            # Enter password
            st_login_password0 = self.wait_for_element(By.ID, "st-lf0-pw0", EC.element_to_be_clickable)
            st_login_password0.send_keys("Password123")
        
            # Click log in button
            self.wait_for_element(By.ID, "st-lf0-s0", EC.element_to_be_clickable).click()
        except:
            assert False, FontModifiers.string_font_bold_red(f"{self._testMethodName}: Testing login form failed") 
        
    def tearDown(self):
        try:
            FontModifiers.font_cyan(f"FINISHED UNIT TEST: {self._testMethodName}") 
            self.driver.quit()
        except:
            assert False, FontModifiers.string_font_bold_red(f"{self._testMethodName}: tearDown() function failed")  

if __name__ == '__main__':
    unittest.main()