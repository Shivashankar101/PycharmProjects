import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select #important#

browser = webdriver.Safari()
browser.get("http://demo.guru99.com/test/newtours/register.php")
browser.implicitly_wait(10)
browser.maximize_window()

ele1 = browser.find_element_by_name("country")
#ele1.click()
# wait = WebDriverWait(browser, 100)
# ele1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='search_str']")))

drop1: Select = Select(ele1)

print(len(drop1.options))
print("options available to select are\n", drop1.options) # notice here

# time.sleep(10)
# # drop1.select_by_index(0)
# WebDriverWait(browser,100).until(EC.visibility_of_all_elements_located((By.NAME, "country")))
# drop1.select_by_visible_text('INDIA')
#THESE ARE NOT WORKING 'VE TO CHECK AGAIN.

for options in drop1.options:
    print(options.text, end="  ##  ", sep=',')     #notice the .text here # here sep="*"do not works, it joins only given items like[1,2,3,4]

####    LINKS   ####

links = browser.find_elements(By.TAG_NAME, "a")
print("\n\n\nno. of links on this page is ", len(links))
print(*[x.text for x in links], sep=" ** ")  #notice the args qwargs and statement

browser.find_element(By.PARTIAL_LINK_TEXT, "Fli").click()

time.sleep(4)
browser.quit()
