import unittest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class FeedbackCRUDTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/login")
        time.sleep(1)

        # login
        self.driver.find_element(By.ID, "username").send_keys("admin")
        self.driver.find_element(By.ID, "password").send_keys("ubtubt123")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(3)

    def test_crud_feedback(self):
        d = self.driver

        # === CREATE ===
        d.get("http://localhost:3000/userfeedback/new")
        time.sleep(2)

        # pick first real user in dropdown
        sel_user = Select(d.find_element(By.NAME, "user"))
        first_val = [o.get_attribute("value") for o in sel_user.options if o.get_attribute("value")][0]
        sel_user.select_by_value(first_val)

        ts           = int(time.time())
        msg_original = f"Selenium feedback {ts}"
        d.find_element(By.NAME, "message").send_keys(msg_original)

        Select(d.find_element(By.NAME, "feedback_type")).select_by_value("suggestion")
        d.find_element(By.TAG_NAME, "form").submit()
        time.sleep(3)

        try:
            d.switch_to.alert.accept()
        except: pass

        self.assertIn("/userfeedback", d.current_url)
        self.assertIn(msg_original, d.page_source)

        # === READ ===
        d.get("http://localhost:3000/userfeedback")
        time.sleep(2)
        self.assertIn(msg_original, d.page_source)

        # === UPDATE ===
        d.find_element(By.XPATH, f"//tr[td/text()='{msg_original}']//button[text()='Edit']").click()
        time.sleep(2)
        msg_updated = f"Përditësuar me Selenium {ts}"
        m = d.find_element(By.NAME, "message")
        m.clear()
        m.send_keys(msg_updated)
        d.find_element(By.TAG_NAME, "form").submit()
        time.sleep(3)

        try:
            d.switch_to.alert.accept()
        except: pass

        self.assertIn("/userfeedback", d.current_url)
        self.assertIn(msg_updated, d.page_source)

        # === DELETE ===
        d.get("http://localhost:3000/userfeedback")
        time.sleep(2)
        d.execute_script("window.confirm = () => true;")
        d.find_element(By.XPATH, f"//tr[td/text()='{msg_updated}']//button[text()='Delete']").click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
