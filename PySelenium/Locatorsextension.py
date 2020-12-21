from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://login.salesforce.com/")

#syntax for generating css selctor from  ID-- tagname#ID
#syntax for generating css from classname tagname.classname

driver.find_element_by_css_selector("#username").send_keys("Namratha")
driver.find_element_by_css_selector(".password").send_keys("12345")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_css_selector(".tn3").click()
#driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_link_text("Forgot Your Password?").click()
#syntax for xpath based on text--- "//tagname[text()='xxx']"
driver.find_element_by_xpath("//*[text()='Cancel']").click()
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
#print(driver.find_element_by_css_selector("form[name='login'] #usernamegroup label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)


#to create xpath and css while tranversing from parent to child tgs
#xpath parenttag/childtag ex: //div[@id='usernamegroup']/label
#css parenttag child tag ex: div[id='usernamegroup'] label
#//form[@name='login']/div[1]/label