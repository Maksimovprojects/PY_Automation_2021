# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# import math

# def calc(x):
#   return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#   browser = webdriver.Chrome()
#   browser.get("http://suninjuly.github.io/math.html")
#
#   x = browser.find_element(By.ID, "input_value").text
#   y = calc(x)
#   input_fieid = browser.find_element(By.ID, "answer")
#   input_fieid.send_keys(y)
#
#   browser.find_element(By.ID, "robotCheckbox").click()
#   browser.find_element(By.ID, "robotsRule").click()
#   button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
#
#
# finally:
#   time.sleep(10)
#   browser.quit()

#--------------------------------------------
#поиск сокровища с помощью get_attribute

from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    treasure = browser.find_element(By.ID, "treasure")
    Find_value_x_inTreasure = treasure.get_attribute("valuex") #true or false
    x = treasure.get_attribute("valuex")
    y = calc(x)
    input_fieid = browser.find_element(By.ID, "answer")
    input_fieid.send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


finally:
  time.sleep(10)
  browser.quit()




