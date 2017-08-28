import unittest
from Page import Page, SignUpPage
from randomemail import generate_email
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignUpUITest(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.driver.maximize_window()
        self.sign_up_page = SignUpPage(self.driver)

    # def test_footer(self):
    #     self.assertIn('©2016 En Masse Entertainment Inc. All Rights Reserved', self.sign_up_page.footer_container.text)
        
    def test_email_taken(self):
        self.sign_up_page.set_email('eme.test@live.com')
        
        self.driver.execute_script("$(#'user_email').focus();")


    # def tearDown(self):
    #     # close the browser window
    #     self.driver.quit()
 
if __name__ == '__main__':
    unittest.main(verbosity=2)