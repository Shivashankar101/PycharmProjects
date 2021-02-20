from selenium import webdriver

driver = webdriver.Safari()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.implicitly_wait(5)

flag = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
#driver.execute_script("window.scrollBy(0,1000)", "")
driver.execute_script("arguments[0].scrollIntoView();", flag)

driver.quit()