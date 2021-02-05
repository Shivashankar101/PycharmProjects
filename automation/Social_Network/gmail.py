from selenium import webdriver

driver = webdriver.Safari()
driver.get('https://twitter.com')
driver.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div").click()
driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]").send_keys('8050430767')
driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div").send_keys('Pgpgpgagj100.')
