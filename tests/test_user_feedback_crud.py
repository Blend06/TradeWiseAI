import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class FeedbackCRUDTest(unittest.TestCase):
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
        time.sleep(2)

    def test_crud_feedback(self):
        driver = self.driver

        # === CREATE ===
        driver.get("http://localhost:3000/userfeedback/new")
        time.sleep(1)

        # Fill form with new data
        select = Select(driver.find_element(By.NAME, "user"))
        select.select_by_value("1")
        driver.find_element(By.NAME, "message").send_keys("Ky është një feedback test nga Selenium")
        select = Select(driver.find_element(By.NAME, "feedback_type"))
        select.select_by_value("suggestion")
        driver.find_element(By.TAG_NAME, "form").submit()
        time.sleep(2)

        try:
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass

        time.sleep(1)
        self.assertIn("userfeedback", driver.current_url)

        # === READ ===
        driver.get("http://localhost:3000/userfeedback")
        time.sleep(1)

        # Check if the feedback exists in the list
        self.assertIn("Ky është një feedback test nga Selenium", driver.page_source)

        # === UPDATE ===
        # Click the first "Edit" button (assumed the one just created)
        edit_button = driver.find_element(By.XPATH, "//button[text()='Edit']")
        edit_button.click()
        time.sleep(1)

        # Update only the `message` field
        message_input = driver.find_element(By.NAME, "message")
        message_input.clear()
        message_input.send_keys("Feedback i përditësuar nga Selenium")
        driver.find_element(By.TAG_NAME, "form").submit()
        time.sleep(2)
        
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass
        time.sleep(1)
        # Verify the update is reflected
        self.assertIn("Feedback i përditësuar nga Selenium", driver.page_source)

        # === DELETE ===
        driver.get("http://localhost:3000/userfeedback")
        time.sleep(1)

        # Inject JavaScript to override confirm() and always return true
        driver.execute_script("window.confirm = function(){ return true; }")

        delete_button = driver.find_element(By.XPATH, "//button[text()='Delete']")
        delete_button.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()