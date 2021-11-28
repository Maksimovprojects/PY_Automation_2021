import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# define function "calc" recognizing math operator and return result between two numbers
def calc(a, b):
    if math_operator == "+":
        result = int(a) + int(b)
    elif math_operator == "-":
        result = int(a) - int(b)
    elif math_operator == "-":
        result = float(a)/ float(b)
    elif math_operator == "*":
        result = float(a) * float(b)
    return result

link  = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
# retrieve value, type, number 1
number1 = browser.find_element(By.ID, "num1").text
# retrieve math operator ("+", "-" etc)
math_operator = browser.find_element(By.CSS_SELECTOR, "h2 > span:nth-child(3)").text
# retrieve value number 2
number2 = browser.find_element(By.ID, "num2").text
sum = calc(number1, number2)
print(sum)
print(type(sum))
sum = str(sum)
select_element = Select(browser.find_element(By.ID, "dropdown"))
# find the element with "sum" value
click_selected_num = select_element.select_by_value(sum)
button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(5)
browser.quit()
