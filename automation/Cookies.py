from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Safari()
driver.get("https://www.amazon.in")
driver.implicitly_wait(10)
driver.maximize_window()


cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

cookie1 = {'name':'Shravan', 'value': 'Hi, how are you'}
driver.add_cookie(cookie1)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

time.sleep(5)

driver.delete_cookie(cookie1)
time.sleep(5)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

time.sleep(5)

driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))


