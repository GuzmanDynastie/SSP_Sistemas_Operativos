import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"./Activities/Classroom/selenium/chromedriver.exe")
        self.driver.maximize_window()

    def test_search(self):
        self.driver.get("http://www.google.com")
        self.assertIn("Google", self.driver.title)

        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium")
        search_box.send_keys(Keys.RETURN)

        # Wait for search results to be visible
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3.LC20lb.DKV0Md")))

        # Check if search results are displayed
        search_results = self.driver.find_elements(By.CSS_SELECTOR, "h3.LC20lb.DKV0Md")
        self.assertTrue(len(search_results) > 0, "No search results found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
