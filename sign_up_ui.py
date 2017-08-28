import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignUpTest(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.base_url = "https://account-edge.enmasse.com/"


    def test_email_taken(self):
        driver = self.driver
        driver.get(self.base_url + "sign-up")
        driver.find_element(By.ID, "user_email").clear()
        driver.find_element(By.ID, "user_email").send_keys("eme.test@live.com")
        driver.find_element(By.ID, "user_email").click()

        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys("P@ssword")

        wait = WebDriverWait(driver, 10)
        wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))
        driver.execute_script("$('#user_email').focus();")

        self.assertIn(("Email has already been taken."), driver.find_element(By.CSS_SELECTOR, 'div.with_errors:nth-child(2)').text)



    def tearDown(self):
        # close the browser window
        self.driver.quit()
 
if __name__ == '__main__':
    unittest.main(verbosity=2)
