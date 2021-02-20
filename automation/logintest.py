import XLUtils
from selenium import webdriver

browser = webdriver.Safari()
browser.get("http://demo.guru99.com/test/newtours/index.php")
browser.maximize_window()


path = "/Users/shiv/desktop/3.xlsx"
for r in range(2, 7):
    user = browser.find_element_by_name("userName")
    pw = browser.find_element_by_name("password")

    id = XLUtils.read_data(path, "login", r, 1)
    password = XLUtils.read_data(path, "login", r, 2)

    user.send_keys(id)
    pw.send_keys(password)

    browser.find_element_by_name("submit").click()

    if browser.title == "Welcome: Mercury Tours":
        XLUtils.write_data(path, "login", r, 3, "test passed")
        print("test passed")
    else:
        XLUtils.write_data(path, "login", r, 3, "failed")
        print("test failed")

    browser.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/font/a").click()
