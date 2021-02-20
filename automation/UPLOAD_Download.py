

# # upload ##
driver.find_element_by_id("id of the upload button").send_keys("path of the file to be uploaded")




# # change Download files path in chrome ##

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory": "/user/downloads"})
driver = webdriver.Chrome(executable_path="User/shiv/chrome/chromedriver", chrome_options=chromeOptions)


# to disable save to disk pop-up while downloading in firefox browser and changing the download file path

from selenium.webdriver.firefox.options import Options as Opt

firefoxOptions = Opt()
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plane,application/pdf")
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", "/user/downloads")

driver = webdriver.Firefox(executable_path="User/shiv/gecko/geckodriver", firefox_options=fp) 
