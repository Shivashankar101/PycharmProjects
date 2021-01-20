
#time.sleep(5) # implicitly_wait #explicitwait --> WebDriverWait.



import time
# from selenium.webdriver.common.keys import Keys
from selenium import webdriver
# from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Safari()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(20)

#input_boxes#
input_boxes = driver.find_elements(By.CLASS_NAME, "nav-input nav-progressive-attribute")
print(f"this page has {len(input_boxes)} input boxes.") #0

driver.maximize_window()
driver.find_element_by_xpath("//*[@id='nav-link-accountList']/div").click()

time.sleep(5)
user_tab = driver.find_element_by_name("email")
user_tab.click()
print("user name tab is enabled :", user_tab.is_enabled())
user_tab.send_keys("8050430767")

time.sleep(5)
driver.find_element_by_xpath("//*[@id='continue']").click() #continue

time.sleep(5) # implicit wait
wait = WebDriverWait(driver, 100)
pwd = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ap_password']")))
pwd.click()
print("user pwd tab is enebled :", pwd.is_enabled())
pwd.send_keys("Pgpgpgagj100.")

driver.find_element_by_xpath("//*[@id='signInSubmit']").click() #login



time.sleep(10)



driver.quit()
