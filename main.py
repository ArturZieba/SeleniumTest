#import stpunittests
import unittest

class TestUnitTesting(unittest.TestCase):
    def setUp(self):
        print("Running unit tests")

    def test_try(self):
        try:
            print("Works")
        except:
            assert False, "Didn't do something"

    def test_try_another(self):
        try:
            print("Works1")
        except:
            assert False, "Didn't do something1"
    
    def tearDown(self):
        print("Finished running unit tests")

        
if __name__ == '__main__':
    unittest.main()

# Open the browser on http://localhost:8000
#stpunittests.launch_browser()

# Open the page with Selenium test elements
#stpunittests.main_to_stp()

##### 

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
#stpunittests.click_buttons()

# Type something into a search bar and opy contents of one search bar into another
#stpunittests.type_in_search_bar()

# Click through the radio buttons
#stpunittests.click_radio_buttons()

# Go through all of the options on a select list
#stpunittests.select_list_select_all_options()

# Enter log in information
#stpunittests.use_login()

# Download an image
#stpunittests.download_image()

# Play through different audio elements
#stpunittests.play_audio_elements()

# Go back to the main page
#stpunittests.stp_to_main()

# Confirm execution of the whole file
#stpunittests.finish_test_run()

