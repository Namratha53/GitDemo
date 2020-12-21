from selenium import  webdriver

val = "Namratha"

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys(val)
driver.find_element_by_css_selector("#alertbtn").click()
al = driver.switch_to.alert
print(al.text)
assert val in al.text
al.accept()

driver.find_element_by_css_selector("#confirmbtn").click()
print(al.text)
al.dismiss()