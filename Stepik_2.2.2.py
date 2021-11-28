import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  browser.get("https://suninjuly.github.io/execute_script.html")
  x = browser.find_element(By.ID, "input_value").text
  y = calc(x)
  input_fieid = browser.find_element(By.ID, "answer")
  input_fieid.send_keys(y)
  browser.execute_script("window.scrollBy(0, 150);")
  browser.find_element(By.ID, "robotCheckbox").click()
  browser.find_element(By.ID, "robotsRule").click()
  button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
  browser.execute_script("return arguments[0].scrollIntoView(true);", button)
  button.click()

finally:
  time.sleep(6)
  browser.quit()