from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

action = ActionChains(driver)

double = driver.find_element_by_id("double-click")
action.double_click(double).perform()
alert = driver.switch_to.alert
#print(alert.text)
action.context_click(double).perform()

assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()
