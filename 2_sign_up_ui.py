import unittest
from Page import Page, SignUpPage
from randomemail import generate_email
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignUpTest(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        # self.driver.maximize_window()


    def test_valid_registration(self):
        sign_up_page = SignUpPage(self.driver)
        self.assertTrue(sign_up_page.signup_wrap.value_of_css_property('display') == 'block')
        sign_up_page.set_email(generate_email())
        sign_up_page.click_element(sign_up_page.user_email_field)
        sign_up_page.page_wait()
        sign_up_page.set_password("P@ssword")
        sign_up_page.page_wait()
        sign_up_page.submit_sign_up()
        WebDriverWait(self.driver, 10).until(EC.visibility_of(sign_up_page.verify_wrap))
        print("Should be here")
        self.assertTrue(sign_up_page.verify_wrap.value_of_css_property('display') == 'block')
        self.assertTrue(sign_up_page.signup_wrap.value_of_css_property('display') == 'none')


        # self.assertIn('Create a free En Masse Account', self.driver.title)

        # elem = self.driver.find_element(By.ID, "user_email")

        # assert elem is not None



    # def tearDown(self):
    #     # close the browser window
    #     self.driver.quit()
 
if __name__ == '__main__':
    unittest.main(verbosity=2)
