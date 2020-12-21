import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)

hover = driver.find_element_by_css_selector("#mousehover")
action.move_to_element(hover).perform()
top = driver.find_element_by_link_text("Top")
time.sleep(2)
action.move_to_element(top).click().perform()
