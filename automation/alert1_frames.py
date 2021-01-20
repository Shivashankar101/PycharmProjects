import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Safari()
browser.get("http://testautomationpractice.blogspot.com")
browser.implicitly_wait(5)
browser.maximize_window()
browser.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
WebDriverWait(browser, 10).until(EC.alert_is_present()).accept()


time.sleep(5)
browser.quit()
