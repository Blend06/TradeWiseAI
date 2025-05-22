from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome options (optional: run headless or not)
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment to run without opening a browser window

# Path to your chromedriver executable
chromedriver_path = "C:/Users/Plus Computers/Desktop/TradeWiseAI/tests/chromedriver.exe"

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("http://localhost:3000/login")

    # Wait a bit to let page load (better to use explicit waits, but this is simple)
    time.sleep(2)

    # Locate inputs by id and fill them
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("admin")      
    password_input.send_keys("ubtubt123")  

    # Click the login button
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # Wait some seconds to observe result or wait for navigation
    time.sleep(5)

    # You can add assertions here if you want to verify successful login by checking URL or elements
    current_url = driver.current_url
    print("Current URL after login attempt:", current_url)

finally:
    driver.quit()
