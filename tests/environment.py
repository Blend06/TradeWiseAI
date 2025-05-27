from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    # Inicializon browserin (Chrome)
    context.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.browser.implicitly_wait(5)  # Koha e pritjes për elementët

def after_all(context):
    context.browser.quit()


