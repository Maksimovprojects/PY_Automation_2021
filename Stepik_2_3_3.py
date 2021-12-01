import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    ListTabs = browser.window_handles  # return list of names of all opened tabs in browser
    # Debug actions
    print(type(ListTabs))  # print on console type of variable
    print(ListTabs)  # print on console each element(names of tabs) in list

    SecondTab = browser.window_handles[1]  # assign "new_window" variable the name of the second
    # element in list of opened tabs
    browser.switch_to.window(SecondTab)  # Switch to window/Tab having tab name assigned to SecondTab

    def calc(num):
        result = str(math.log(abs(12 * math.sin(int(num)))))
        return result

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    input_fieid = browser.find_element(By.ID, "answer")
    input_fieid.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    time.sleep(3)
    browser.quit()