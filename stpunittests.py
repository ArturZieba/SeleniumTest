# Module containing unit tests for the Selenium Test page

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from shutil import copyfileobj
from support import FontModifiers
import time
import unittest
from urllib.request import urlopen



class Tests(unittest.TestCase):
    def setUp(self):
        try:
            FontModifiers.font_cyan("SCRIPTS EXECUTION START") # Rewrite?

            # Open Dev Tools
            chrome_options = Options()
            chrome_options.add_argument("--auto-open-devtools-for-tabs")

            service = Service(executable_path="chromedriver.exe") # chromedriver.exe downloaded from https://sites.google.com/chromium.org/driver/
            self.driver = webdriver.Chrome(service=service, options=chrome_options)

            self.driver.get("http://localhost:8000")
            time.sleep(1) # Chceck WebDriverWait?

            # Open the page with Selenium test elements
            link_to_test_page = self.driver.find_element(By.LINK_TEXT, "Selenium Test Page").click()
            time.sleep(3) # Chceck WebDriverWait
        except:
            assert False, FontModifiers.font_bold_red("Didn't reach Selenium Test Page") # Rewrite? AssertionError: None?  
    
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
            st_red_button = self.driver.find_element(By.ID, "st-b0").click()
            time.sleep(1) # Chceck WebDriverWait?
    
            st_green_button = self.driver.find_element(By.ID, "st-b1").click()
            time.sleep(1) # Chceck WebDriverWait?
    
            st_blue_button = self.driver.find_element(By.ID, "st-b2").click()
            time.sleep(1) # Chceck WebDriverWait?
        except:
            assert False, FontModifiers.font_bold_red("Clicking buttons failed") # Rewrite? AssertionError: None?
    
    # Type and copy/paste something into a search bar
    def test_type_in_search_bar(self):
        try:
            st_search_bar0 = self.driver.find_element(By.ID, "st-sb0")
            st_search_bar0.send_keys("Hello, World!")
            time.sleep(1)
        
            # Copy contents of one search bar into another
            st_search_bar0.send_keys(Keys.CONTROL, "a")
            st_search_bar0.send_keys(Keys.CONTROL, Keys.SHIFT, "j")
            time.sleep(1)
            st_search_bar0.send_keys(Keys.CONTROL, "c")
            time.sleep(1)
        
            st_search_bar1 = self.driver.find_element(By.ID, "st-sb1")
            st_search_bar1.send_keys(Keys.CONTROL, "v")
            time.sleep(1)
        except:
            assert False, FontModifiers.font_bold_red("Search Bar typing or copy/pasting failed") # Rewrite? AssertionError: None?
    
    # Click through the radio buttons
    def test_click_radio_buttons(self):
        try:
            st_radio_button0 = self.driver.find_element(By.ID, "st-rb1").click()
            time.sleep(1)
        
            st_radio_button1 = self.driver.find_element(By.ID, "st-rb0").click()
            time.sleep(1)
        
            st_radio_button2 = self.driver.find_element(By.ID, "st-rb2").click()
            time.sleep(1)
        except:
            assert False, FontModifiers.font_bold_red("Clicking radio buttons failed") # Rewrite? AssertionError: None?
    
    # Go through all of the options on a select list
    def test_select_list_select_all_options(self):
        try:
            st_select_list = self.driver.find_element(By.ID, "st-sl0")
            select_element_sl0 = Select(st_select_list)
        
            select_element_sl0_options = select_element_sl0.options
        
            for option in select_element_sl0_options:
                select_element_sl0.select_by_value(option.get_attribute('value'))
                time.sleep(1)
        except:
            assert False, FontModifiers.font_bold_red("Selecting from a select list failed") # Rewrite? AssertionError: None?
    
    # Enter log in information
    def test_use_login(self):
        try:
            st_login_username0 = self.driver.find_element(By.ID, "st-lf0-un0")
            st_login_username0.send_keys("BobOfficial")
            time.sleep(1)
        
            st_login_password0 = self.driver.find_element(By.ID, "st-lf0-pw0")
            st_login_password0.send_keys("Password123")
            time.sleep(1)
        
            st_login_submit_0 = self.driver.find_element(By.ID, "st-lf0-s0").click()
            time.sleep(1)
        except:
            assert False, FontModifiers.font_bold_red("Testing login form failed") # Rewrite? AssertionError: None?    
    
    # Download an image
    def test_download_image(self):
        try:
            st_image0_url = self.driver.find_element(By.ID, "st-img0").get_attribute("src")
            time.sleep(1)
        
            with urlopen(st_image0_url) as in_stream, open("downloaded_bober.png", "wb") as out_file:
                copyfileobj(in_stream, out_file)
            time.sleep(1)
        except:
            assert False, FontModifiers.font_bold_red("Downloading an image failed") # Rewrite? AssertionError: None?  
    
    # Play through different audio elements
    #def play_audio_elements(self):
    #    driver.execute_script("document.querySelector('#st-af0').play();")
    #    time.sleep(0.5)
    #    driver.execute_script("document.querySelector('#st-af0').volume = 0.5;")
    #    time.sleep(0.5)
    #    driver.execute_script("document.querySelector('#st-af0').pause();")
    #    time.sleep(0.5)
    #    driver.execute_script("document.querySelector('#st-af0').play();")
    #    time.sleep(4)
    #    driver.execute_script("document.querySelector('#st-af1').play();")
    #    time.sleep(5)
    #    driver.execute_script("document.querySelector('#st-af2').play();")
    #    time.sleep(5)
    
    # Go back to the main page
    #def stp_to_main(self):
    #    link_to_main_page = driver.find_element(By.LINK_TEXT, "AZ Main Page").click()
    #time.sleep(1)
    
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
        self.driver.quit() # Is the browser restart on each case the best way to do it?

if __name__ == '__main__':
    unittest.main()