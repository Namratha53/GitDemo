from selenium import webdriver

# browser exposes an executable file
# through selenium  test we need to invoke that executable file which will then invoke the actual browser
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
#driver = webdriver.Firefox(executable_path='C:\\geckodriver.exe')
driver.maximize_window()
driver.get('https://www.udemy.com/')

print(driver.title)
print(driver.current_url)
driver.get('https://www.udemy.com/courses/development/')
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()
