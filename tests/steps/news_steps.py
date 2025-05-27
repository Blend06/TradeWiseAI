from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

BASE_URL = "http://localhost:3000"

@given('I am logged in as admin for news')
def step_impl(context):
    context.browser.get(f"{BASE_URL}/login")

    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )

    context.browser.find_element(By.ID, "username").send_keys("admin")
    context.browser.find_element(By.ID, "password").send_keys("ubtubt123")

    context.browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(context.browser, 10).until(
        EC.url_to_be(f"{BASE_URL}/")
    )

    context.browser.get(f"{BASE_URL}/news")

    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

@given('I am on the News list page')
def step_impl(context):
    context.browser.get(f"{BASE_URL}/news")
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

@when('I navigate to the new news article form')
def step_impl(context):
    new_btn = context.browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')
    new_btn.click()
    WebDriverWait(context.browser, 10).until(
        EC.url_contains("/news/new")
    )
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "title"))
    )
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "content"))
    )
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "image"))
    )

@when('I fill in title "{title}", content "{content}", and upload image "{image_filename}"')
def step_impl(context, title, content, image_filename):
    title_input = context.browser.find_element(By.ID, "title")
    title_input.clear()
    title_input.send_keys(title)

    content_input = context.browser.find_element(By.ID, "content")
    content_input.clear()
    content_input.send_keys(content)

    image_input = context.browser.find_element(By.ID, "image")
    # Assuming the images are in a folder "test_images" in the project root
    image_path = os.path.abspath(os.path.join("test_images", image_filename))
    image_input.send_keys(image_path)

@when('I submit the news form')
def step_impl(context):
    submit_btn = context.browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

    # Handle success alert if present
    try:
        WebDriverWait(context.browser, 5).until(EC.alert_is_present())
        alert = context.browser.switch_to.alert
        alert_text = alert.text
        print(f"Alert appeared with text: {alert_text}")
        alert.accept()
    except:
        print("No alert appeared after form submission.")

    # Proceed to wait for page change and article list
    WebDriverWait(context.browser, 15).until(
        EC.url_to_be(f"{BASE_URL}/news")
    )
    WebDriverWait(context.browser, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr"))
    )

@then('I should see the new news article with title "{title}" in the list')
@then('I should see the news article with title "{title}" in the list')
def step_impl(context, title):
    WebDriverWait(context.browser, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "table"), title)
    )
    table = context.browser.find_element(By.TAG_NAME, "table")
    assert title in table.text, f"Expected to find news article title '{title}' in list."

@then('I should not see the news article with title "{title}" in the list')
def step_impl(context, title):
    table = context.browser.find_element(By.TAG_NAME, "table")
    assert title not in table.text, f"Did not expect to find news article title '{title}' in list."

@then('I should see a list of news articles displayed')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr"))
    )
    rows = context.browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    assert len(rows) > 0, "Expected at least one news article in the list."

@given('a news article with title "{title}" exists')
def step_impl(context, title):
    context.execute_steps(f'''
        Given I am on the News list page
    ''')
    table = context.browser.find_element(By.TAG_NAME, "table")
    if title not in table.text:
        context.execute_steps(f'''
            When I navigate to the new news article form
            And I fill in title "{title}", content "Sample content for {title}", and upload image "test-image.jpg"
            And I submit the news form
        ''')
    WebDriverWait(context.browser, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "table"), title)
    )

@when('I navigate to edit the news article with title "{title}"')
def step_impl(context, title):
    rows = context.browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    found = False
    print("Looking for title:", title)
    for row in rows:
        print("Row content:", row.text)
        if title in row.text:
            edit_btn = row.find_element(By.XPATH, ".//button[contains(@class, 'btn-warning')]")
            edit_btn.click()

            WebDriverWait(context.browser, 10).until(
                EC.presence_of_element_located((By.ID, "title"))
            )
            found = True
            break
    assert found, f"Could not find news article with title '{title}' to edit."

@when('I change the title to "{new_title}"')
def step_impl(context, new_title):
    title_input = context.browser.find_element(By.ID, "title")
    title_input.clear()
    title_input.send_keys(new_title)

@when('I change the content to "{new_content}"')
def step_impl(context, new_content):
    content_input = context.browser.find_element(By.ID, "content")
    content_input.clear()
    content_input.send_keys(new_content)

@when('I delete the news article with title "{title}"')
def step_impl(context, title):
    rows = context.browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    found = False
    for row in rows:
        if title in row.text:
            delete_btn = row.find_element(By.CSS_SELECTOR, "button.btn-danger")
            delete_btn.click()
            alert = context.browser.switch_to.alert
            alert.accept()
            WebDriverWait(context.browser, 10).until(
                EC.staleness_of(row)
            )
            found = True
            break
    assert found, f"Could not find news article with title '{title}' to delete."
