import selenium
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#driver = webdriver.Chrome()
#
# url = 'https://iol1.iroquois.com/infopost/Pages/OperationallyAvailable.php?parentId=100'
# browser.get(url)

#driver = webdriver.Firefox (executable_path = "/users/shiv/desktop/drivers/gecko/geckodriver.exe" )
#driver = webdriver.Chrome (executable_path = "/users/shiv/desktop/drivers/gecko/geckodriver.exe" )

driver = webdriver.Safari()
#WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
# driver.get("http://automationtesting.in/")
#
# print(driver.title)
#
# driver.find_element_by_xpath("//*[@id='menu-icon']").click()
# print(driver.current_url)


driver.get("https://www.amazon.in/")

driver.maximize_window()



driver.find_element_by_xpath("//*[@id='nav-link-accountList']/div").click()
time.sleep(5)


user_tab = driver.find_element_by_name("email")
time.sleep(5)
user_tab.click()
time.sleep(5)
print("user name tab is enabled :", user_tab.is_enabled())
time.sleep(1)
user_tab.send_keys("8050430767")

driver.find_element_by_xpath("///*[@id='continue']").click()

#show_pwd = driver.find_element_by_xpath("//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div/input")
# print("show password box  tab is selected :",show_pwd.is_selected())

pwd = driver.find_element_by_name("password")
pwd.click()
print("user name tab is enebled :", user_tab.is_enabled())
time.sleep(2)
pwd.send_keys("Pgpgpgagj100.")

driver.find_element_by_xpath("//*[@id='signInSubmit']").click()

time.sleep(2)

driver.back()

driver.quit()
