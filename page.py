from time import sleep
from element import BasePageElement
from locators import LoginPageLocators, MainPageLocators, HomePageLocators
from selenium.webdriver.common.action_chains import ActionChains
# The page file currently contains all the information for the various pages that are accessed during the test
# In a real world test suite this would not be sustainable so would likely separate it out for each page.

# BasePage contains functions that will be used on all screens
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

    def click_login_button(self):
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login.click()

    def error_displayed(self):
        error_message = self.driver.find_element(*LoginPageLocators.LOGIN_ERROR_TEXT).text
        return "We didn't recognize that email and/or password. Need help?" in error_message
        
    enter_email = email_field()
    enter_password = password_field()