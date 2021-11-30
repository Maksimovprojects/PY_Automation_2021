import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  browser.get("http://suninjuly.github.io/alert_accept.html")
  button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
  button.click()
  confirm = browser.switch_to.alert #switch to pop-up Alert window
  confirm.accept()
  x = browser.find_element(By.ID, "input_value").text
  y = calc(x)
  input_fieid = browser.find_element(By.ID, "answer")
  input_fieid.send_keys(y)
  button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
  button.click()

finally:
  time.sleep(6)
  browser.quit()


