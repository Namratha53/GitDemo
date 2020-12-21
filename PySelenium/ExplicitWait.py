import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

list1=[]
list2=[]
amount=[]

driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input[type='search']").send_keys('br')
time.sleep(3)

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
print(len(buttons))
count = len(buttons)
assert count==2
#//div[@class='product-action']/button/parent::div/parent::div/h4

for but in buttons:
    list1.append(but.find_element_by_xpath("parent::div/parent::div/h4").text)
    but.click()
print(list1)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver,8)
wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, "input.promocode")))
before = driver.find_element_by_css_selector("span.discountAmt").text
veggies = driver.find_elements_by_xpath("//p[@class='product-name']")
for veg in veggies:
    list2.append(veg.text)
print(list2)
driver.find_element_by_css_selector("input.promocode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()
wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, "span.promoInfo")))
after=driver.find_element_by_css_selector("span.discountAmt").text

assert  int(before) >float(after)

print(driver.find_element_by_css_selector("span.promoInfo").text)

#//table[@class='cartTable']/tbody/tr/td[5]
#//tr/td[5]/p

totalAmt= int(driver.find_element_by_css_selector("span.totAmt").text)
amounts = driver.find_elements_by_xpath("//table[@class='cartTable']/tbody/tr/td[5]")
sum=0
for amt in amounts:
    sum+=int(amt.text)

print(sum)

assert sum==totalAmt





