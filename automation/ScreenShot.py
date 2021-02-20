from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Safari()
driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()
time.sleep(10)
#WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]")))
driver.save_screenshot("/Users/shiv/PycharmProjects/automation/screenshots/a.png")
# driver.get_screenshot_as_file("/Users/shiv/PycharmProjects/automation/screenshots/a.png")  # we can also use this
