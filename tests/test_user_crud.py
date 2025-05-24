import unittest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserCRUDTest(unittest.TestCase):
    def setUp(self):
        print("\n[SETUP] Launching browser and logging in…")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/login")
        time.sleep(1)
        print("[LOGIN] Entering credentials")
        self.driver.find_element(By.ID, "username").send_keys("admin")
        self.driver.find_element(By.ID, "password").send_keys("ubtubt123")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(3)  # land on /controlpanel
        print("[LOGIN] Completed")

    def _accept_alert_if_any(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
        except:
            pass

    def test_crud_user(self):
        d = self.driver

        # === CREATE ===
        print("[CREATE] Navigating to new user form")
        d.get("http://localhost:3000/users/new")
        time.sleep(2)
        ts       = int(time.time())
        username = f"testuser{ts}"
        email    = f"user{ts}@example.com"
        print(f"[CREATE] Filling form with username={username}, email={email}")
        d.find_element(By.NAME, "username").send_keys(username)
        d.find_element(By.NAME, "email").send_keys(email)
        d.find_element(By.NAME, "password").send_keys("SecurePass1")
        print("[CREATE] Submitting form")
        d.find_element(By.TAG_NAME, "form").submit()
        self._accept_alert_if_any()
        time.sleep(2)
        print("[CREATE] Verifying creation")
        self.assertIn("/users", d.current_url)
        self.assertIn(username, d.page_source)
        print("[CREATE] Passed")

        # === READ ===
        print("[READ] Loading users list")
        d.get("http://localhost:3000/users")
        time.sleep(2)
        print("[READ] Verifying user presence")
        self.assertIn(username, d.page_source)
        print("[READ] Passed")

        # === UPDATE ===
        print("[UPDATE] Clicking edit for our user")
        d.find_element(By.XPATH, f"//tr[td/text()='{username}']//button[text()='Edit']").click()
        time.sleep(2)
        new_email = f"upd{ts}@example.com"
        print(f"[UPDATE] Changing email to {new_email}")
        e = d.find_element(By.NAME, "email")
        e.clear()
        e.send_keys(new_email)
        print("[UPDATE] Submitting update")
        d.find_element(By.TAG_NAME, "form").submit()
        self._accept_alert_if_any()
        time.sleep(2)
        print("[UPDATE] Verifying update")
        self.assertIn("/users", d.current_url)
        self.assertIn(new_email, d.page_source)
        print("[UPDATE] Passed")

        # === DELETE ===
        print("[DELETE] Removing the test user")
        d.get("http://localhost:3000/users")
        time.sleep(2)
        d.execute_script("window.confirm = () => true;")
        d.find_element(By.XPATH, f"//tr[td/text()='{username}']//button[text()='Delete']").click()
        time.sleep(3)
        print("[DELETE] Done")

    def tearDown(self):
        print("[TEARDOWN] Closing browser")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
