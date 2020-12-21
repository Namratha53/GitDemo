from selenium import webdriver

driver =  webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element_by_link_text("Click Here").click()

child = driver.window_handles[1] #list which stores IDs of parent and child. generally index 0 is parent consecutive by child IDs

driver.switch_to.window(child)

print(driver.find_element_by_tag_name("h3").text)

driver.close()

driver.switch_to.window(driver.window_handles[0])

assert driver.find_element_by_tag_name("h3").text == "Opening a new window"