from element import BasePageElement
from locators import LoginPageLocators, MainPageLocators

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def does_title_match(self, title):
        return title in self.driver.title
    
class MainPage(BasePage):
    def click_login_button(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()

class LoginPage(BasePage):
    class email_field(BasePageElement):
        locator = LoginPageLocators.EMAIL_FIELD

    class password_field(BasePageElement):
        locator = LoginPageLocators.PASSWORD_FIELD

    enter_email = email_field()
    enter_password = password_field()