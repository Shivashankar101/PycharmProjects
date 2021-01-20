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

# gmail = driver.find_element(By.XPATH, "/html/body/footer/div[3]/div/a[1]/img")
# # gmail = driver.find_element_by_link_text("/html/body/footer/div[3]/div/a[1]/img")
# gmail.click()
# WebDriverWait(driver, 100).until(EC.new_window_is_opened())
#THIS IS NOT WORKING

handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()

time.sleep(2)
driver.quit()