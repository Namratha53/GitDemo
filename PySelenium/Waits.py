import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input[type='search']").send_keys('br')
time.sleep(3)

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
print(len(buttons))
count = len(buttons)
assert count==2

for but in buttons:
    but.click()


driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_css_selector("input.promocode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()
print(driver.find_element_by_css_selector("span.promoInfo").text)
