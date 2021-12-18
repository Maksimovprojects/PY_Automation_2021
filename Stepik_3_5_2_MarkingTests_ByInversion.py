import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser...")
    browser.quit()

@pytest.mark.TestMainPage1 # marking for executing tests into class (check marker into file pytest.ini)
class TestMainPage1():

    @pytest.mark.smoke # marking (smoke) for executing test into method (check marker into file pytest.ini)
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.smoke # marking (regression) for executing test into method (check marker into file pytest.ini)
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

# cmd in terminal: (pytest -s -v -m "not smoke" test_fixture8.py), Run exception tests
# cmd in terminal: (pytest -s -v -m "smoke or regression" test_fixture8.py), Will Run smoke Regression
# cmd in terminal: (pytest -s -v -m "smoke and win10" test_fixture81.py). Run test having ONLY both params smoke and win10


