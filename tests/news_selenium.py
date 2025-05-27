import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class NewsCRUDTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/login")
        time.sleep(1)
        
        # Login
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("ubtubt123")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(3)

    def test_crud_news(self):
        driver = self.driver

        # === CREATE ===
        driver.get("http://localhost:3000/news/new")
        time.sleep(2)

        title_text = "Lajm Test nga Selenium"
        content_text = "Ky është përmbajtja e lajmit të testuar me Selenium."

        # Fill form
        driver.find_element(By.NAME, "title").send_keys(title_text)
        driver.find_element(By.NAME, "content").send_keys(content_text)

        # Upload an image (use any small sample image path on your machine)
        image_path = os.path.abspath("sample.jpg")
        driver.find_element(By.NAME, "image").send_keys(image_path)

        # Submit form
        driver.find_element(By.TAG_NAME, "form").submit()
        time.sleep(3)

        # Handle alert
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass

        self.assertIn("/news", driver.current_url)

        # === READ ===
        driver.get("http://localhost:3000/news")
        time.sleep(2)
        self.assertIn(title_text, driver.page_source)

        # === UPDATE ===
        edit_button = driver.find_element(By.XPATH, "//button[text()='Edit']")
        edit_button.click()
        time.sleep(2)

        updated_content = "Përmbajtja u përditësua me Selenium"

        content_input = driver.find_element(By.NAME, "content")
        content_input.clear()
        content_input.send_keys(updated_content)
        driver.find_element(By.TAG_NAME, "form").submit()
        time.sleep(3)

        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass

        self.assertIn("/news", driver.current_url)
        self.assertIn(updated_content, driver.page_source)

        # === DELETE ===
        driver.get("http://localhost:3000/news")
        time.sleep(2)

        # Override confirm popup
        driver.execute_script("window.confirm = function(){ return true; }")
        delete_button = driver.find_element(By.XPATH, "//button[text()='Delete']")
        delete_button.click()
        time.sleep(3)

        

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
