"Test for https://the-internet.herokuapp.com/digest_auth"

import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestDigestAuth(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_digest_auth(self):
        driver = self.driver
        username = "admin"
        password = "admin"
        url = f"https://{username}:{password}@the-internet.herokuapp.com/digest_auth"
        
        driver.get(url)

        screenshot_path = os.path.join(os.getcwd(), "screenshot.png")
        driver.save_screenshot(screenshot_path)
        
        success_message = driver.find_element(By.TAG_NAME, "p").text
        self.assertIn("Congratulations", success_message)

    def tearDown(self):
        
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()