import unittest
from Page import Page, SignUpPage
from randomemail import generate_email
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class ValidRegistrationTest(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_valid_registration(self):
        sign_up_page = SignUpPage(self.driver)
        self.assertTrue(sign_up_page.signup_wrap.value_of_css_property('display') == 'block')
        sign_up_page.set_email(generate_email())
        # sign_up_page.click_element(sign_up_page.user_email_field)
        sign_up_page.page_wait()
        sign_up_page.set_password("P@ssword")
        sign_up_page.page_wait()
        sign_up_page.submit_sign_up()
        WebDriverWait(self.driver, 10).until(EC.visibility_of(sign_up_page.verify_wrap))
        self.assertTrue(sign_up_page.verify_wrap.value_of_css_property('display') == 'block')
        self.assertTrue(sign_up_page.signup_wrap.value_of_css_property('display') == 'none')

    # def test_facebook_registration(self):
    #     sign_up_page = SignUpPage(self.driver)
    #     self.assertTrue(sign_up_page.signup_wrap.value_of_css_property('display') == 'block')
    #     primary_window = sign_up_page.driver.window_handles[0]
    #     sign_up_page.click_element(sign_up_page.facebook_register)
    #     fb_window = sign_up_page.driver.window_handles[1]
    #     sign_up_page.driver.switch_to.window(fb_window)
    #     sign_up_page.send_input(sign_up_page.driver.find_element_by_id('email'), 'openrjam@yahoo.com')
    #     sign_up_page.send_input(sign_up_page.driver.find_element_by_id('pass'), '7Du74neG')
    #     sign_up_page.driver.find_element_by_id('pass').submit()
    #     sign_up_page.driver.find_element_by_name('__CONFIRM__').click()
    #     sign_up_page.driver.switch_to.window(primary_window)
    #     Select(sign_up_page.driver.find_element_by_id('user_secret_question_id')).select_by_value('1')
    #     sign_up_page.send_input(sign_up_page.driver.find_element_by_id('user_secret_answer'), 'test')
    #     sign_up_page.driver.find_element_by_id('user_secret_answer').submit()




    # def tearDown(self):
    #     # close the browser window
    #     self.driver.quit()
 
if __name__ == '__main__':
    unittest.main(verbosity=2)
