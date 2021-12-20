import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Catch message in specific areas *feedback(

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('path', ["236895/step/1", "236896/step/1", "236897/step/1", "236898/step/1",
                                  "236899/step/1", "236903/step/1", "236904/step/1", "236905/step/1"])
def test_guest_should_see_login_link(browser, path):
    answer = math.log(int(time.time()))
    link = f"https://stepik.org/lesson/{path}/"
    browser.implicitly_wait(5)
    browser.get(link)    # get a link for test
    input_field = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Type your answer here...']")  # find text input(field) element
    input_field.send_keys(answer)  # send answer to that field
    browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()  # click "submit button"
    message = browser.find_element(By.CSS_SELECTOR, "pre.smart-hints__hint").text
    assert "Correct!" == message, "other message"