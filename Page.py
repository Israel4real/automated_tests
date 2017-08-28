from locators import SignUpLocators
from selenium.webdriver.support.ui import WebDriverWait

class Page():
    "Page class that all page models can inherit from"

    def __init__(self,driver, base_url='https://account-edge.enmasse.com/'):
        "Constructor"
        self.driver = driver
        self.base_url = base_url
        #Visit and initialize for appropriate page
        self.start()

    def open(self, url):
        "Visit the page url"
        url = self.base_url + url
        self.driver.get(url)
 
 
    def click_element(self,element):
        "Click the element supplied"
        element.click()

    def send_input(self, element, user_input):
        "Send keys to field"
        element.send_keys(user_input)

    def page_wait(self):
        "Wait for jquery to finish"
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: self.driver.execute_script("return jQuery.active == 0"))

class SignUpPage(Page):
    "Standard EME Sign Up page object"

    def start(self):
        "Initilization"
        self.url = "sign-up"
        self.open(self.url)

        self.signup_wrap = self.driver.find_element(*SignUpLocators.signup_wrap)
        self.verify_wrap = self.driver.find_element(*SignUpLocators.verify_wrap)
        self.user_email_field = self.driver.find_element(*SignUpLocators.user_email_field)
        self.user_password_field = self.driver.find_element(*SignUpLocators.user_password_field)
        self.submit_button = self.driver.find_element(*SignUpLocators.submit_button)
        self.facebook_register = self.driver.find_element(*SignUpLocators.facebook_register)
        self.resend_verification = self.driver.find_element(*SignUpLocators.resend_verification)
        self.footer_container = self.driver.find_element(*SignUpLocators.footer_container)

    def set_email(self, email):
        "Set email"
        self.send_input(self.user_email_field, email)

    def set_password(self, password):
        "Set password"
        self.send_input(self.user_password_field, password)

    def submit_sign_up(self):
        "Submit registration"
        self.click_element(self.submit_button)

    def submit_facebook(self):
        self.click_element(self.facebook_register)






