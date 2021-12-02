import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    element_price = browser.find_element(By.ID, "price")
    price_element = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    book_button = browser.find_element(By.ID, "book").click()

    # scroll on 400 pixels
    browser.execute_script("window.scrollBy(0, 400);")

    def calc(num):
        result = str(math.log(abs(12 * math.sin(int(num)))))
        return result
    x = browser.find_element(By.ID, "input_value").text

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(calc(x))
    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    time.sleep(5)
    browser.quit()