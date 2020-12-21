from selenium import webdriver

driver =  webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
count = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(count))

for i in count:
    print(i.get_attribute('value'))
    if i.get_attribute('value') == 'option2':
        i.click()
        assert i.is_selected()
        break

radiobox = driver.find_elements_by_name('radioButton')
for j in radiobox:
    if j.get_attribute('value') == 'radio2':
        j.click()
        break

check = driver.find_element_by_id("displayed-text")

assert check.is_displayed()

driver.find_element_by_css_selector("#hide-textbox").click()

check = driver.find_element_by_id("displayed-text")

assert not check.is_displayed()


