from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import page
import time

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.hudl.com")
        self.wait = WebDriverWait(self.driver, 10)

    def test_login_hudl_user(self):
        driver = self.driver
        
        main_page = page.MainPage(self.driver)
        assert main_page.does_title_match("Performance analysis tools for sports teams and athletes at every level."), "Title does not match"
        main_page.click_login_button()

        login_page = page.LoginPage(self.driver)
        assert login_page.does_title_match("Log In - Hudl"), "Title does not match"

        login_page.enter_email = "redacted"
        login_page.enter_password = "redacted"
        login_page.click_login_button()

        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()