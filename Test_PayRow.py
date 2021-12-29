from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

# XPATH
# Marked 1 uniq "Get_Started_Button", because we do have 3 the same buttons on the page
Get_Started = "//div[@class = 'HeaderPages-MiddleContent-Wrapper']/*[contains(text(), 'Get started')]"
Login = "//*[@at-id='button-login']"
Yes_button = "//button[contains(text(), 'Yes')]"
No_button = "//button[contains(text(), 'No')]"
LoginForm = "//h1[contains(text(), 'Login to Payrow')]"
Business_Form = "//h1[contains(text(), 'Business account')]"
Disclaimer_Form = "//h1[contains(text(),'If you are not')]"
# URL
Login_Url = "https://payrow.com/main/auth/sign-in"
Main_Page_Url = "https://payrow.com/business"
Get_Started_Url = "https://payrow.com/main/auth/create-account/eligibility"
Create_Account_Url = "https://payrow.com/main/auth/create-account/eligibility"

class TestPayRow(unittest.TestCase):

    def test_check_login_and_getstarted_buttons_mainPage(self):
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(Main_Page_Url)
            button_get_started = browser.find_element(By.XPATH, Get_Started)
            button_login = browser.find_element(By.XPATH, Login)
            assert button_get_started.is_displayed(), "Button 'Get_Started' isn't displayed"
            assert button_login.is_displayed(), "Button 'Login' isn't displayed"
        finally:
            browser.quit()

    def test_check_redirection_from_main_to_login(self):
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(Main_Page_Url)
            go_to_login = browser.find_element(By.XPATH, Login)
            go_to_login.click()
            assert browser.current_url == Login_Url, "Login url is not presented"
        finally:
            browser.quit()

    def test_check_login_form_is_presented(self):
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(Login_Url)
            login_form_message = browser.find_element(By.XPATH, LoginForm).text
            assert login_form_message == "Login to Payrow", "Login form is not presented"
        finally:
            browser.quit()

    def test_check_redirection_from_mainpage_to_get_started(self):
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(Main_Page_Url)
            go_to_get_started = browser.find_element(By.XPATH, Get_Started)
            go_to_get_started.click()
            get_started_page = browser.window_handles[1]
            main_page = browser.window_handles[0]
            browser.switch_to.window(main_page)
            browser.close()
            browser.switch_to.window(get_started_page)
            assert browser.current_url == Get_Started_Url, "Get_Started url is not presented"
        finally:
            browser.quit()

    def test_availability_yes_no_buttons_on_create_account_page(self):
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(Get_Started_Url)
            find_no = browser.find_element(By.XPATH, No_button)
            find_yes = browser.find_element(By.XPATH, Yes_button)
            assert find_yes.is_displayed(), "'Yes' button isn't displayed"
            assert find_no.is_displayed(), "'No' button isn't displayed"
        finally:
            browser.quit()

    def test_check_business_form_by_yes_btn_from_create_account_page(self):
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(Create_Account_Url)
            find_yes = browser.find_element(By.XPATH, Yes_button)
            find_yes.click()
            business_form_message = browser.find_element(By.XPATH, Business_Form).text
            assert business_form_message == "Business account", "Business form is not presented"
        finally:
            browser.quit()

    def test_check_disclaimer_form_by_no_btn_from_create_account_page(self):
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(Create_Account_Url)
            find_no = browser.find_element(By.XPATH, No_button)
            find_no.click()
            disclaimer_form_message = browser.find_element(By.XPATH, Disclaimer_Form).text
            print(disclaimer_form_message)
            assert disclaimer_form_message == "If you are not\n currently eligible", "Disclaimer form is not presented"
        finally:
            browser.quit()


if __name__ == "__main__":
    unittest.main()
