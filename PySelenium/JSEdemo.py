from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("Nammu")
print(driver.find_element_by_name("name").get_attribute('value'))

print(driver.execute_script('return document.getElementsByName("name")[0].value'))

#selenium doesn't support SCROLLING!!!
shop = driver.find_element_by_xpath("//ul[@class='navbar-nav']/li[2]/a")
driver.execute_script("arguments[0].click();", shop)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
