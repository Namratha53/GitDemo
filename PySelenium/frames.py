from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#frame,frameset,iframe
driver.get("https://the-internet.herokuapp.com/iframe")
#either pass frame ids, frame names, index values
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("Hi, there! welcome :)")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)
