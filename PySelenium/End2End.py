import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click()

products = driver.find_elements_by_xpath("//div[@class='card h-100']")

#//div[@class='card h-100']/div/h4/a
for product in products:
    print(product.find_element_by_xpath("div/h4/a").text)
    var = product.find_element_by_xpath("div/h4/a").text
    if var == "Blackberry":
# //div[@class='card h-100']/div/button
        time.sleep(2)
        product.find_element_by_xpath("div/button").click()
        break
driver.find_element_by_xpath("//a[contains(text(),'Checkout')]").click()
#button[class*='btn-success']
driver.find_element_by_css_selector("button[class*='btn-success']").click()
driver.find_element_by_css_selector("#country").send_keys("ind")
wait=WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text('India').click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("input[type='submit']").click()
successs = (driver.find_element_by_xpath("//div[contains(@class, 'alert-success')]").text)

assert "Success! Thank you!" in successs

driver.get_screenshot_as_file("Testscreenshot.png")







