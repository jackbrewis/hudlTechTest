from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_BUTTON = (By.CLASS_NAME, "btn__blue.login")

class LoginPageLocators(object):
    EMAIL_FIELD = "username"
    PASSWORD_FIELD = "password"
    LOGIN_BUTTON = (By.CLASS_NAME, "btn-orange.btn-block")