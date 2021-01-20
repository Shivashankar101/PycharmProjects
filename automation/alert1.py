import time
from selenium import webdriver

browser = webdriver.Safari()
browser.get("http://testautomationpractice.blogspot.com")
browser.implicitly_wait(5)
browser.maximize_window()

browser.switch_to_alert().accept()   #.dismiss()

time.sleep(2)
browser.quit()
