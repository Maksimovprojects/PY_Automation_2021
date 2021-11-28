import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# TASK3
# CHECKING REQUIRED FIELDS

# VARIABLES
FirstNameData = "First_name"
LastNameData = "Last_name"
EmailData = "12345@12345.com"
link = "http://suninjuly.github.io/registration1.html"


# XPATHes
xPath_FirstName = '//input[@placeholder="Input your first name"]'
xPath_LastName = '//input[@placeholder="Input your last name"]'
xPath_Email = '//input[@placeholder="Input your email"]'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # My code fills all required fields
    InputFirstName = browser.find_element(By.XPATH, xPath_FirstName)
    InputFirstName.send_keys(FirstNameData)
    InputLastName = browser.find_element(By.XPATH, xPath_LastName)
    InputLastName.send_keys(LastNameData)
    InputEmailData = browser.find_element(By.XPATH, xPath_Email)
    InputEmailData.send_keys(EmailData)

    # checking register possibility
    # wait till page will upload
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(10)

    # find element by tag having the text
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # writing variable welcome_text, message from element welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #waiting for visually score results of finished scripts
    time.sleep(5)
    # close browser
    browser.quit()


