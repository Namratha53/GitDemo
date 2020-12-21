from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')

driver.get('https://rahulshettyacademy.com/angularpractice/')

#locators are used to find the location in which we need to fill some details in a website for example name, DOB
#address etc, find_element_by_name is one of them.
#types of locators: ID,name,xpath,CSS,classname,linktext
#syntax for CSS selectors --- "tagname[attribute='value']" for reg ex-- "tagname[attribute*='value']"
#syntax for Xpath---- '//tagname[@attribute='value']" for reg ex--- "//*[contains(@attribute,'value')]"



#driver.find_element_by_css_selector("input[name='name']").send_keys('Namratha')
driver.find_element_by_css_selector("input[name='name']").send_keys('Nammu')
driver.find_element_by_id('exampleCheck1').click()
dropdown = Select(driver.find_element_by_id('exampleFormControlSelect1'))
dropdown.select_by_visible_text('Female')
dropdown.select_by_index(0)
driver.find_element_by_name('email').send_keys('Cerner')
driver.find_element_by_xpath("//input[@type='submit']").click()
#print(driver.find_element_by_css_selector("div[class*='alert-success']").text)  #css locator
message = driver.find_element_by_xpath("//*[contains(@class,'alert-success')]").text  #xpath

assert 'success' in message
