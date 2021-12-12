from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestStepikWebSite(unittest.TestCase):

    def RegisterForm_NameFirstEmailPhoneAddress(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        InputFirstName = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
        InputFirstName.send_keys("Ivan")
        InputLastName = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        InputLastName.send_keys("Ivanov")
        InputEmailData = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        InputEmailData.send_keys("12345@12345.com")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        browser.quit()

    def RegisterForm_NameFirstLastEmailPhoneAddress(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        InputFirstName = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
        InputFirstName.send_keys("Ivan")
        InputEmailData = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        InputEmailData.send_keys("12345@12345.com")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        browser.quit()

if __name__ == "__main__":
    unittest.main()
