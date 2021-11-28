import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#TASK 1
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.TAG_NAME, "input")
#     for element in elements:
#         element.send_keys("myAnswer")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     time.sleep(30)
#     browser.quit()
#
#--------------------------------------------------------------------------------


#TASK 2

#VARIABLES
# value1 = "input"
# value2 = "last_name"
# value3 = "city"
# value4 = "country"
# xPath_button = '//button[@type="submit"]'
# browser = webdriver.Chrome()
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/find_xpath_form")
#     input1 = browser.find_element(By.TAG_NAME, value1)
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, value2)
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, value3)
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, value4)
#     input4.send_keys("Russia")
#     button = browser.find_element(By.XPATH, xPath_button).click()
#
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

#--------------------------------------------------------------------------

#TASK3  
#CHECKING REDUIRED FIELDS

#VARIABLES
FirstNameData = "First_name"
LastNameData = "Last_name"
EmailData = "12345@12345.com"

# XPATHes
xPath_FirstName = '//input[@placeholder="Input your first name"]'
xPath_LastName = '//input[@placeholder="Input your last name"]'
xPath_Email = '//input[@placeholder="Input your email"]'

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #My code fills all fields
    InputFirstName = browser.find_element(By.XPATH, xPath_FirstName)
    InputFirstName.send_keys(FirstNameData)
    InputLastName = browser.find_element(By.XPATH, xPath_LastName)
    InputLastName.send_keys(LastNameData)
    InputEmailData = browser.find_element(By.XPATH, xPath_Email)
    InputEmailData.send_keys(EmailData)

    #checking register possibility
    #wait till page will upload
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(10)

    #find element by tag having the text
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    #writting variable welcome_text, message from element welcome_text_elt
    welcome_text = welcome_text_elt.text
    
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    
    