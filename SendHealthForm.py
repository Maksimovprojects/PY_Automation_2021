from selenium import webdriver
import time
from selenium.webdriver.common.by import By


#Xpathes
email_field = '//input[@type = "email"]'
name_selector = "body.freebirdLightBackground:nth-child(5) div.freebirdFormviewerViewFormContentWrapper:nth-child(9) div.freebirdFormviewerViewCenteredContent div.freebirdFormviewerViewFormCard.exportFormCard:nth-child(2) div.freebirdFormviewerViewFormContent div.freebirdFormviewerViewItemList:nth-child(2) div.freebirdFormviewerViewNumberedItemContainer:nth-child(2) div.m2 div.freebirdFormviewerComponentsQuestionBaseRoot.hasError div.freebirdFormviewerComponentsQuestionTextRoot div.quantumWizTextinputPaperinputEl.freebirdFormviewerComponentsQuestionTextShort.freebirdFormviewerComponentsQuestionTextTextInput.freebirdThemedInput.modeLight div.quantumWizTextinputPaperinputMainContent.exportContent div.quantumWizTextinputPaperinputContentArea.exportContentArea div.quantumWizTextinputPaperinputInputArea > input.quantumWizTextinputPaperinputInput.exportInput"



#VALUES
email_data = "maximebayer@gmail.com"
name_data = "Maksim Maksimov"
value3 = "city"
value4 = "country"
value5 = "button.btn"
link = "https://docs.google.com/forms/d/e/1FAIpQLSec8IlhamjNAsnq7ucQnlZXuigvNcAh1OUiVmqmc_E3x0SXfg/viewform"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.XPATH, email_field)
    input1.send_keys(email_data)


    input2 = browser.find_element(By.CSS_SELECTOR, name_selector)
    input2.send_keys(name_data)
    #
    # input3 = browser.find_element(By.CLASS_NAME, value3)
    # input3.send_keys("Smolensk")
    #
    # input4 = browser.find_element(By.ID, value4)
    # input4.send_keys("Russia")
    #
    # button = browser.find_element(By.CSS_SELECTOR, value5)
    # button.click()

finally:
    time.sleep(5)
    browser.quit()

