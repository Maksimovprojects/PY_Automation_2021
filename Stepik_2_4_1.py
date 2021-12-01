from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")
    browser.implicitly_wait(5)
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")
    #assert "successful" in message.text, "TEST FAILED"
    assert "Verification was successful!" == message.text, "TEST FAILED"

finally:
    browser.quit()