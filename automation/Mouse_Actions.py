from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
#driver = webdriver.Chrome(executable_path="/Users/shiv/desktop/drivers/chrome/chromedriver")
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//*[@id='btnLogin']").click()

Admin = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu_admin_viewAdminModule']/b")))
#Admin = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
Usr = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
menu = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")



acts = ActionChains(driver)
acts.move_to_element(Admin).move_to_element(Usr).move_to_element(menu).click().perform()
time.sleep(3)
driver.close()

### DOUBLE CLICK ####
# driver.findElement(By.linkText("http://testautomationpractice.blogspot.com")).sendKeys(selectLinkOpeninNewTab)
# # driver.get("http://testautomationpractice.blogspot.com")
# # click = WebDriverWait(driver, 100).until(EC.ele
# click = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
#acts.double_click(click).perform()

# RIGHT CLICK
# acts.context_click(click).perform()


