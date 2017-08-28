import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignUpTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # navigate to the application home page
        # cls.driver.get("https://account-edge.enmasse.com/tera/sign-up")
        cls.driver.title

    # def test_game_logo(self):
    #     """Game logo present"""
    #     self.driver.get("https://account-edge.enmasse.com/tera/sign-up")
    #     game_logo = self.driver.find_elements_by_class_name("game_logo")
    #     self.assertTrue(game_logo)

    def test_facebook_register_button(self):
        pass

    # def test_form_signup(self):
    #     """Email and Password fields present"""
    #     self.driver.find_element(By.ID, "user_email").send_keys("test17@alt.com")
    #     self.driver.find_element(By.ID, "user_email").click()
    #     # self.driver.find_element(By.ID, "user_email").send_keys("test5@alt.com")
    #     self.driver.find_element(By.ID, "user_password").send_keys("P@ssword")
    #     self.driver.find_element(By.ID, "btn-create-account").click()



    #     # email_sent = self.driver.find_element(By.ID, "email_address")
    #     verification_link = self.driver.find_element(By.LINK_TEXT, "Resend Verification Email")
    #     print('Element Text: ' + verification_link.get_attribute('href'))

    def test_email_taken(self):
        self.driver.get("https://account-edge.enmasse.com/sign-up")
        self.driver.find_element(By.ID, "user_email").clear()
        self.driver.find_element(By.ID, "user_email").send_keys("eme.test@live.com")
        self.driver.find_element(By.ID, "user_email").click()

        self.driver.find_element_by_id("user_password").clear()
        self.driver.find_element_by_id("user_password").send_keys("P@ssword")

        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: self.driver.execute_script("return jQuery.active == 0"))
        self.driver.execute_script("$('#user_email').focus();")

        self.assertIn("Email has already been taken.", self.driver.find_element(By.CSS_SELECTOR, 'div.with_errors:nth-child(2)').text)

    def test_email_reserved(self):
        self.driver.get("https://account-edge.enmasse.com/sign-up")
        self.driver.find_element(By.ID, "user_email").clear()
        self.driver.find_element(By.ID, "user_email").send_keys("test@enmasse.com")
        self.driver.find_element(By.ID, "user_email").click()

        self.driver.find_element_by_id("user_password").clear()
        self.driver.find_element_by_id("user_password").send_keys("P@ssword")

        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: self.driver.execute_script("return jQuery.active == 0"))
        self.driver.execute_script("$('#user_email').focus();")

        self.assertIn("reserved", self.driver.find_element(By.CSS_SELECTOR, 'div.with_errors:nth-child(2)').text)

    def test_ui_elements(self):
        self.assertEqual("©2017 En Masse Entertainment Inc. All Rights Reserved", self.driver.find_element_by_css_selector("div.disclaimer > p").text)



    # @classmethod
    # def tearDownClass(cls):
    #     # close the browser window
    #     cls.driver.quit()
 
if __name__ == '__main__':
    unittest.main(verbosity=2)
