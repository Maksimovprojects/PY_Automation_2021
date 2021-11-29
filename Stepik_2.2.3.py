import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# TASK 2.2.3
# Checking uploading form

# DATA VARIABLES
FirstNameData = "John"
LastNameData = "Smith"
EmailData = "12345@12345.com"
link = "http://suninjuly.github.io/file_input.html"

# CSS Selectors
FirstNameSelector = 'input[name = firstname]'
LastNameSelector = 'input[name = lastname]'
EmailSelector = 'input[name = email]'
ChooseFileSelector = 'input[name = file]'
SubmitButtonSelector = 'button[type=submit]'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # My code fills all required fields
    InputFirstName = browser.find_element(By.CSS_SELECTOR, FirstNameSelector)
    InputFirstName.send_keys(FirstNameData)
    InputLastName = browser.find_element(By.CSS_SELECTOR, LastNameSelector)
    InputLastName.send_keys(LastNameData)
    InputEmailData = browser.find_element(By.CSS_SELECTOR, EmailSelector)
    InputEmailData.send_keys(EmailData)
    browser.find_element(By.xpath)



    #Create testfile.txt
    with open('testfile.txt', 'w') as file1:
        file1.write('text for mls 228')
    print("file 'testfile.txt' created")

    # Find path to text.txt file
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    print("--------demarcation----------")
    print(os.path.abspath(__file__))
    print("--------demarcation----------")
    file_path = os.path.join(current_dir, 'testfile.txt')  # добавляем к этому пути имя файла
    print(os.path.abspath(os.path.dirname(__file__)))
    print("--------demarcation----------")

    # Find CSS locator and send file path
    ChooseFileButton = browser.find_element(By.CSS_SELECTOR, ChooseFileSelector)
    ChooseFileButton.send_keys(file_path)

    # Click Submit for getting a code
    SubmitButton = browser.find_element(By.CSS_SELECTOR, SubmitButtonSelector).click()

    #remove testfile.txt file
    os.remove(file_path)
    print("file 'testfile.txt' deleted")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #waiting for visually score results of finished scripts
    time.sleep(5)
    # close browser
    browser.quit()


