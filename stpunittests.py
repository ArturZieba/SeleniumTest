# Module containing unit tests for the Selenium Test page

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
            # chrome_options.add_argument("--auto-open-devtools-for-tabs") # Potential chromedriver/chrome verisons mismatch, comment out for the time being

            service = Service(executable_path="chromedriver.exe") # chromedriver.exe downloaded from https://sites.google.com/chromium.org/driver/
            self.driver = webdriver.Chrome(service=service, options=chrome_options)

            self.driver.get("http://localhost:8000")

            # Open the page with Selenium test elements
            self.wait_for_element(By.LINK_TEXT, "Selenium Test Page", EC.element_to_be_clickable).click()
        except:
            assert False, FontModifiers.string_font_bold_red("Didn't reach Selenium Test Page") # Rewrite?   
    
    ##### 
    
    # Change the unit tests to be executed one by one in a single browser window instead of launching multiple ones?
    # time.sleep value in a variable?
    # Check unit testing
    # Add a counter to try/except for all cases
    # Move FontModifiers to separate file along with its test?
    # Try/except to verify the tests executed?
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
            assert False, FontModifiers.string_font_bold_red("Invalid: Clicking buttons failed") # Rewrite? 
    
    # Type and copy/paste something into a search bar
    def test_type_in_search_bar(self):
        try:
            st_search_bar0 = self.wait_for_element(By.ID, "st-sb0", EC.element_to_be_clickable)
            st_search_bar0.send_keys("Hello, World!")
        
            # Copy contents of one search bar into another
            # More clear formatting?
            st_search_bar0.send_keys(Keys.CONTROL, "a")
            st_search_bar0.send_keys(Keys.CONTROL, Keys.SHIFT, "j")
            st_search_bar0.send_keys(Keys.CONTROL, "c")
        
            st_search_bar1 = self.wait_for_element(By.ID, "st-sb1", EC.element_to_be_clickable)
            st_search_bar1.send_keys(Keys.CONTROL, "v")
            
        except:
            assert False, FontModifiers.string_font_bold_red("Search Bar typing or copy/pasting failed") # Rewrite? 
    
    # Click through the radio buttons
    def test_click_radio_buttons(self):
        try:
            self.wait_for_element(By.ID, "st-rb1", EC.element_to_be_clickable).click()
        
            self.wait_for_element(By.ID, "st-rb0", EC.element_to_be_clickable).click()
        
            self.wait_for_element(By.ID, "st-rb2", EC.element_to_be_clickable).click()
        except:
            assert False, FontModifiers.string_font_bold_red("Clicking radio buttons failed") # Rewrite? 
    
    # Go through all of the options on a select list
    def test_select_list_select_all_options(self):
        try:
            st_select_list = self.wait_for_element(By.ID, "st-sl0", EC.element_to_be_clickable)
            select_element_sl0 = Select(st_select_list)
        
            select_element_sl0_options = select_element_sl0.options
        
            for option in select_element_sl0_options:
                select_element_sl0.select_by_value(option.get_attribute('value'))
        except:
            assert False, FontModifiers.string_font_bold_red("Selecting from a select list failed") # Rewrite? 
    
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
            assert False, FontModifiers.string_font_bold_red("Testing login form failed") # Rewrite?     
    
    # Download an image
    def test_download_image(self):
        try:
            st_image0_url = self.driver.find_element(By.ID, "st-img0").get_attribute("src")
            time.sleep(1)
        
            with urlopen(st_image0_url) as in_stream, open("downloaded_bober.png", "wb") as out_file:
                copyfileobj(in_stream, out_file)
            time.sleep(1)
        except:
            assert False, FontModifiers.string_font_bold_red("Downloading an image failed") # Rewrite?   
    
    # Play through different audio elements
    def test_play_audio_elements(self):
        try:
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
            assert False, FontModifiers.string_font_bold_red("Playing audio elements failed") # Rewrite? 
    
    # Go back to the main page
    def test_stp_to_main(self):
        try:
            self.wait_for_element(By.LINK_TEXT, "AZ Main Page", EC.element_to_be_clickable).click()
        except:
            assert False, FontModifiers.string_font_bold_red("Going back to main page failed") # Rewrite? 
    
    #def finish_test_run(self):
        # Confirm execution of the whole file
        # If statement with count of passed/failed tests?
    #    FontModifiers.font_cyan("ALL SCRIPTS EXECUTED")
        # if (fail_count == 0):
        #     FontModifiers.font_green("ALL " + str(test_count) + " TEST CASES PASSED")
        # else:
        #     FontModifiers.font_red(str((test_count - fail_count)) + " / " + str(test_count) + " TEST CASES PASSED")
    #    time.sleep(3)
    
    #    driver.quit()
        
    def tearDown(self):
        FontModifiers.font_cyan("END OF UNIT TESTS") # Rewrite? 
        # Add assertion?
        
        self.driver.quit() # Is the browser restart on each case the best way to do it?

if __name__ == '__main__':
    unittest.main()