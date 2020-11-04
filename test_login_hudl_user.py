from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import page

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.hudl.com")
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(10)

        # All login tests will need to navigate to the login page, therefore making that step in the setup
        main_page = page.MainPage(self.driver)
        assert main_page.does_title_match("Performance analysis tools for sports teams and athletes at every level."), "Title does not match"
        main_page.click_login_button()

    def test_login_hudl_user(self):

        login_page = page.LoginPage(self.driver)
        assert login_page.does_title_match("Log In - Hudl"), "Title does not match"

        login_page.enter_email = "jackbrewis96@gmail.com"
        login_page.enter_password = "Ao3G8&KLItHbNX&0"
        login_page.click_login_button()

        home_page = page.HomePage(self.driver)
        # Very messy solution, definitely would clean up in a real test suite however I could 
        sleep(2)
        assert home_page.check_team_name("QA Hire Project"), "Team name does not match"
        assert home_page.does_title_match("Home - Hudl"), "Title does not match"

    def test_login_error(self):

        login_page = page.LoginPage(self.driver)
        assert login_page.does_title_match("Log In - Hudl"), "Title does not match"

        login_page.enter_email = "jackbrewis96@gmail.com"
        login_page.enter_password = "Ao3G8&KLItHbNX&"
        login_page.click_login_button()

        sleep(2)
        assert login_page.error_displayed(), "Error message was not displayed"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()