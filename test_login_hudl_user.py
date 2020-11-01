import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login_hudl_user(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.get("http://www.hudl.com")
        self.assertIn("Performance analysis tools for sports teams and athletes at every level.", driver.title)
        loginButton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn__blue.login')))
        loginButton.click()
        self.assertIn("Log In - Hudl", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()