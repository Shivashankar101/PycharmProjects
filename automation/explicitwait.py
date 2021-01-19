

#wait.WebDriver() # explict wait

import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Firefox(executable_path="/users/shiv/desktop/drivers/gecko/geckodriver.exe")
browser.get("http://www.expedia.com/")
browser.implicitly_wait(10)
browser.maximize_window()

time.sleep(5)
browser.find_element(By.XPATH, "//*[@id='uitk-tabs-button-container']/li[2]/a").click()


from_tab = browser.find_element(By.XPATH, "//*[@id='location-field-leg1-origin-menu']/div[1]/button")
from_tab.click()
from_tab.send_keys("NYC")
# from_tab.send_keys(Keys.ENTER)
#
# drop1 = Select(from_tab)
# print(len(drop1.options))
# drop1.options

'''
#browser.find_element(By.XPATH, "//*[@id='location-field-leg1-origin-menu']/div[2]/ul/li[1]/button").click()
browser.find_element(By.XPATH, "//*[@id='location-field-leg1-destination-menu']/div[1]/button").send_keys("BKK")
#browser.find_element(By.XPATH, "//*[@id='location-field-leg1-destination-menu']/div[2]/ul/li[1]/button").click()


browser.find_element(By.XPATH, "//*[@id='d1-btn']").click()
browser.find_element(By.XPATH, "//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[2]/button").click()
browser.find_element(By.XPATH, "//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[3]/button").click()
browser.find_element(By.XPATH, "//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div/div[3]/button/span").click()

browser.find_element(By.XPATH, "//*[@id='stops-1']").click()
'''

# //*[@id="wizard-hotel-pwa-v2-1"]/div[1]/div[1]/div/div/div/div/div/button
browser.quit()