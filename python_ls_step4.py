from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

#VARIABLES
value1 = "input"
value2 = "last_name"
value3 = "city"
value4 = "country"
value5 = "button.btn"
browser = webdriver.Chrome()

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")
    browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e) * 10000))).click()

    input1 = browser.find_element(By.TAG_NAME, value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, value4)
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, value5)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

#_________________________________________________________

