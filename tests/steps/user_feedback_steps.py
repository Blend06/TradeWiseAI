from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://localhost:3000"

@given('I am on the User Feedback list page')
def step_impl(context):
    context.browser.get(f"{BASE_URL}/userfeedback")
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

@when('I navigate to the new feedback form')
def step_impl(context):
    new_btn = context.browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')
    new_btn.click()
    WebDriverWait(context.browser, 10).until(
        EC.url_contains("/userfeedback/new")
    )
    # Crucial waits for the form elements to be present and ready
    # Wait for the 'user' select element to be present
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "user"))
    )
    # Wait for at least one actual user option to be loaded in the 'user' select dropdown
    # This specifically looks for an <option> inside the <select id="user"> that has a non-empty 'value' attribute
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#user option[value]:not([value=''])"))
    )
    # Wait for the 'message' textarea
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "message"))
    )
    # Wait for the 'feedback_type' select
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "feedback_type"))
    )

@when('I fill in user "{user_id}", message "{message}", feedback type "{feedback_type}"')
def step_impl(context, user_id, message, feedback_type):
    # Ensure the user select element is clickable before interacting
    user_select = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.ID, "user"))
    )
    for option in user_select.find_elements(By.TAG_NAME, "option"):
        if option.get_attribute("value") == user_id:
            option.click()
            break

    message_input = context.browser.find_element(By.ID, "message")
    message_input.clear()
    message_input.send_keys(message)

    feedback_select = context.browser.find_element(By.ID, "feedback_type")
    for option in feedback_select.find_elements(By.TAG_NAME, "option"):
        if option.get_attribute("value") == feedback_type:
            option.click()
            break

@when('I submit the feedback form')
def step_impl(context):
    submit_btn = context.browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()
    # Wait for the URL to change back to the list page after submission
    WebDriverWait(context.browser, 10).until(
        EC.url_to_be(f"{BASE_URL}/userfeedback")
    )

@then('I should see the new feedback with message "{message}" in the list')
@then('I should see the feedback with message "{message}" in the list')
def step_impl(context, message):
    # Wait for the table to be present and for the message to appear in the table text
    WebDriverWait(context.browser, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "table"), message)
    )
    table = context.browser.find_element(By.TAG_NAME, "table")
    assert message in table.text, f"Expected to find message '{message}' in feedback list."

@then('I should not see the feedback with message "{message}" in the list')
def step_impl(context, message):
    # Wait for the table to update and for the message to NOT be present
    # This might require a small delay or a more sophisticated wait if the element disappears slowly
    # For now, we'll assert directly after the initial table check.
    table = context.browser.find_element(By.TAG_NAME, "table")
    assert message not in table.text, f"Did not expect to find message '{message}' in feedback list."

@then('I should see a list of feedbacks displayed')
def step_impl(context):
    # Wait for at least one row in the table body to ensure data is displayed
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr"))
    )
    rows = context.browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    assert len(rows) > 0, "Expected at least one feedback in the list."

@given('a feedback with message "{message}" exists')
def step_impl(context, message):
    context.execute_steps(f'''
        Given I am on the User Feedback list page
    ''')
    table = context.browser.find_element(By.TAG_NAME, "table")
    if message not in table.text:
        context.execute_steps(f'''
            When I navigate to the new feedback form
            And I fill in user "1", message "{message}", feedback type "suggestion"
            And I submit the feedback form
        ''')
    # After potentially adding feedback, wait for the table to update with the new entry
    WebDriverWait(context.browser, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "table"), message)
    )

@when('I navigate to edit the feedback with message "{message}"')
def step_impl(context, message):
    rows = context.browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    found_feedback = False
    for row in rows:
        if message in row.text:
            edit_btn = row.find_element(By.CSS_SELECTOR, "button.btn-warning")
            edit_btn.click()
            # Wait for the URL to contain the edit path
            WebDriverWait(context.browser, 10).until(
                EC.url_contains("/userfeedback/edit/")
            )
            # Crucial waits for the form elements on the edit page to be present and ready
            # Wait for the 'user' select element
            WebDriverWait(context.browser, 10).until(
                EC.presence_of_element_located((By.ID, "user"))
            )
            # Wait for at least one actual user option to be loaded in the 'user' select dropdown on the edit page
            WebDriverWait(context.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#user option[value]:not([value=''])"))
            )
            # Wait for the 'message' textarea
            WebDriverWait(context.browser, 10).until(
                EC.presence_of_element_located((By.ID, "message"))
            )
            # Wait for the 'feedback_type' select
            WebDriverWait(context.browser, 10).until(
                EC.presence_of_element_located((By.ID, "feedback_type"))
            )
            found_feedback = True
            break
    assert found_feedback, f"Could not find feedback with message '{message}' to edit."

@when('I change the message to "{new_message}"')
def step_impl(context, new_message):
    message_input = context.browser.find_element(By.ID, "message")
    message_input.clear()
    message_input.send_keys(new_message)

@when('I delete the feedback with message "{message}"')
def step_impl(context, message):
    rows = context.browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    found_feedback = False
    for row in rows:
        if message in row.text:
            # Corrected CSS selector for the delete button
            delete_btn = row.find_element(By.CSS_SELECTOR, "button.btn-danger")
            delete_btn.click()
            # Handle the JavaScript alert for confirmation
            alert = context.browser.switch_to.alert
            alert.accept()
            # Wait for the specific row to disappear from the DOM after deletion
            WebDriverWait(context.browser, 10).until(
                EC.staleness_of(row)
            )
            found_feedback = True
            break
    assert found_feedback, f"Could not find feedback with message '{message}' to delete."