from selenium.webdriver.common.by import By

class SignUpLocators():
    user_email_field = (By.ID, 'user_email')
    user_password_field = (By.ID, 'user_password')
    submit_button = (By.ID, 'btn-create-account')
    facebook_register = (By.XPATH, '//*[@id="app-account"]/section/div/div/div[1]/a')
    verify_wrap = (By.ID, 'verify-wrap')
    signup_wrap = (By.CLASS_NAME, 'signup-wrap')
    resend_verification = (By.XPATH, '//*[@id="verify-wrap"]/p[2]/a')
    footer_container = (By.XPATH, '//*[@id="eme-footer"]/div/div/p')
