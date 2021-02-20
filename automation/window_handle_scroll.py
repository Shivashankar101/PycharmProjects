from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("http://demo.automationtesting.in/Windows.html")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)
driver.current_window_handle
WebDriverWait(driver, 100).until(EC.new_window_is_opened())

# # scroll down the page by pixel
# driver.execute_script("window.scrollBy(0,1000)", "")


testbird = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/a/img")
# # scroll down the page until element is found
driver.execute_script("arguments[0].scrollIntoView();", testbird)
testbird.click()

# # scroll down to the page end of page
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

# handles = driver.window_handles
#
# for handle in handles:
#     driver.switch_to.window(handle)
#     print(driver.title)
#     if driver.title == "Frames & windows":
#         driver.close()

time.sleep(2)
driver.quit()