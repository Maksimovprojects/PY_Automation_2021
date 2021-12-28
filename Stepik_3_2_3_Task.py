import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

# TASK3
# CHECKING REQUIRED FIELDS

# VARIABLES
FirstNameData = "First_name"
LastNameData = "Last_name"
EmailData = "12345@12345.com"
link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


# XPATHes
xPath_FirstName = '//input[@placeholder="Input your first name"]'
xPath_LastName = '//input[@placeholder="Input your last name"]'
xPath_Email = '//input[@placeholder="Input your email"]'

class Test_Page(unittest.TestCase):

    def test_send_data_page1(self):
        browser = webdriver.Chrome()
        browser.get(link1)
        # My code fills all required fields
        InputFirstName = browser.find_element(By.XPATH, xPath_FirstName)
        InputFirstName.send_keys(FirstNameData)
        InputLastName = browser.find_element(By.XPATH, xPath_LastName)
        InputLastName.send_keys(LastNameData)
        InputEmailData = browser.find_element(By.XPATH, xPath_Email)
        InputEmailData.send_keys(EmailData)
        # checking register possibility
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        # wait till page will upload
        time.sleep(5)
        # find element by tag having the text
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # writing variable welcome_text, message from element welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        time.sleep(5)
        browser.quit()

    def test_send_data_page2(self):
        browser = webdriver.Chrome()
        browser.get(link2)
        # My code fills all required fields
        InputFirstName = browser.find_element(By.XPATH, xPath_FirstName)
        InputFirstName.send_keys(FirstNameData)
        InputLastName = browser.find_element(By.XPATH, xPath_LastName)
        InputLastName.send_keys(LastNameData)
        InputEmailData = browser.find_element(By.XPATH, xPath_Email)
        InputEmailData.send_keys(EmailData)
        # checking register possibility
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        # wait till page will upload
        time.sleep(5)
        # find element by tag having the text
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # writing variable welcome_text, message from element welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        #assert "Congratulations! You have successfully registered!" == welcome_text
        time.sleep(5)
        browser.quit()

if __name__ == "__main__":
    unittest.main()