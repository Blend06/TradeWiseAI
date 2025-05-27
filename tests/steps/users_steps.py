from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoAlertPresentException

BASE_URL = "http://localhost:3000"

@given('I am logged in as admin for users')
def step_impl(context):
    context.browser.get(f"{BASE_URL}/login")
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, "username")))

    context.browser.find_element(By.ID, "username").send_keys("admin")
    context.browser.find_element(By.ID, "password").send_keys("ubtubt123")

    context.browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(context.browser, 10).until(EC.url_to_be(f"{BASE_URL}/"))

@given('I am on the Users list page')
def step_impl(context):
    context.browser.get(f"{BASE_URL}/users")
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))

@when('I navigate to the new user form')
def step_impl(context):
    new_btn = context.browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')
    new_btn.click()
    WebDriverWait(context.browser, 10).until(EC.url_contains("/users/new"))
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, "username")))

@when('I fill in username "{username}", email "{email}", password "{password}"')
def step_impl(context, username, email, password):
    context.new_username = username  # store for later use

    username_input = context.browser.find_element(By.ID, "username")
    username_input.clear()
    username_input.send_keys(username)

    email_input = context.browser.find_element(By.ID, "email")
    email_input.clear()
    email_input.send_keys(email)

    password_input = context.browser.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys(password)

@when('I submit the user form')
def step_impl(context):
    submit_btn = context.browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

    try:
        WebDriverWait(context.browser, 5).until(EC.alert_is_present())
        alert = context.browser.switch_to.alert
        alert_text = alert.text
        print(f"Alert appeared with text: {alert_text}")
        alert.accept()
    except TimeoutException:
        print("No alert appeared after form submission.")

    username = getattr(context, 'new_username', None)

    def user_row_contains_username(driver):
        try:
            rows = driver.find_elements(By.CSS_SELECTOR, "tbody tr")
            for row in rows:
                if username and username in row.text:
                    return True
            return False
        except Exception:
            return False

    try:
        WebDriverWait(context.browser, 15).until(
            EC.url_to_be(f"{BASE_URL}/users")
        )
    except TimeoutException:
        if username:
            WebDriverWait(context.browser, 15).until(user_row_contains_username)
        else:
            raise AssertionError("Timeout waiting for users page or user list update after submitting form.")

    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr"))
    )

@then('I should see the new user with username "{username}" in the list')
def step_impl(context, username):
    table_locator = (By.TAG_NAME, "table")

    def user_row_contains_username(driver):
        try:
            table = driver.find_element(*table_locator)
            rows = table.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                if username in row.text:
                    return True
            return False
        except Exception as e:
            print(f"Exception in checking table rows: {e}")
            return False

    WebDriverWait(context.browser, 20).until(user_row_contains_username)
    table_text = context.browser.find_element(*table_locator).text
    assert username in table_text
@then('I should see the user with username "{username}" and email "{email}" in the list')
def step_impl(context, username, email):
    table_locator = (By.TAG_NAME, "table")

    def user_row_contains_username_and_email(driver):
        try:
            table = driver.find_element(*table_locator)
            rows = table.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                if username in row.text and email in row.text:
                    return True
            return False
        except Exception as e:
            print(f"Exception in checking table rows: {e}")
            return False

    WebDriverWait(context.browser, 20).until(user_row_contains_username_and_email)
    table_text = context.browser.find_element(*table_locator).text
    assert username in table_text and email in table_text
@given('a user with username "{username}" exists')
def step_impl(context, username):
    context.execute_steps(f'''
        Given I am on the Users list page
    ''')
    table = context.browser.find_element(By.TAG_NAME, "table")
    if username not in table.text:
       context.execute_steps(f'''
    When I navigate to the new user form
    And I fill in username "{username}", email "temp@example.com", password "J7hyuititi"
    And I submit the user form
''')
    WebDriverWait(context.browser, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "table"), username)
    )

@when('I navigate to edit the user with username "{username}"')
def step_impl(context, username):
    rows = context.browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    found = False
    for row in rows:
        if username in row.text:
            edit_btn = row.find_element(By.XPATH, ".//button[contains(@class, 'btn-warning')]")
            edit_btn.click()
            WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, "username")))
            found = True
            break
    assert found, f"Could not find user with username '{username}' to edit."

@when('I change the email to "{new_email}"')
def step_impl(context, new_email):
    email_input = context.browser.find_element(By.ID, "email")
    email_input.clear()
    email_input.send_keys(new_email)

@when('I change the password to "{new_password}"')
def step_impl(context, new_password):
    password_input = context.browser.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys(new_password)


@when('I delete the user with username "{username}"')
def step_impl(context, username):
    rows = context.browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    found = False
    for row in rows:
        if username in row.text:
            delete_btn = row.find_element(By.CSS_SELECTOR, "button.btn-danger")
            delete_btn.click()

            alert = context.browser.switch_to.alert
            alert.accept()

            # Wait for the row to disappear (staleness)
            WebDriverWait(context.browser, 10).until(EC.staleness_of(row))

            # Additional wait for table to update and username to be gone
            def username_not_present(driver):
                table = driver.find_element(By.TAG_NAME, "table")
                return username not in table.text

            WebDriverWait(context.browser, 20).until(username_not_present)

            found = True
            break
    assert found, f"Could not find user with username '{username}' to delete."

@then('I should not see the user with username "{username}" in the list')
def step_impl(context, username):
    table_locator = (By.TAG_NAME, "table")
    
    def user_not_in_table(driver):
        try:
            table = driver.find_element(*table_locator)
            return username not in table.text
        except Exception as e:
            print(f"Exception while checking user absence: {e}")
            return False
    
    WebDriverWait(context.browser, 20).until(user_not_in_table)
    table_text = context.browser.find_element(*table_locator).text
    assert username not in table_text

@then('I should see a list of users displayed')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr")))
    rows = context.browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    assert len(rows) > 0, "Expected at least one user in the list."