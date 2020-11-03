from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_BUTTON = (By.CLASS_NAME, "btn__blue.login")

class LoginPageLocators(object):
    EMAIL_FIELD = "username"
    PASSWORD_FIELD = "password"
    LOGIN_BUTTON = (By.CLASS_NAME, "btn-orange.btn-block")
    LOGIN_ERROR_TEXT = (By.XPATH, "//div[@class='login-error-container']//p")

class HomePageLocators(object):
    USER_DROPDOWN = (By.CLASS_NAME, "hui-globalusermenu")
    EMAIL_TEXT = (By.CLASS_NAME, "hui-globaluseritem__email")