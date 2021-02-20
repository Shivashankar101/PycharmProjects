from selenium import webdriver

browser = webdriver.Chrome(executable_path="/Users/shiv/desktop/drivers/chrome/chromedriver")
browser.get("https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India")
browser.implicitly_wait(10)
# browser.maximize_window()

row = len(browser.find_elements_by_xpath("//*[@id='mw-content-text']/div[1]/table[2]/tbody/tr"))
# blocks = len(browser.find_elements_by_xpath("//*[@id='mw-content-text']/div[1]/table[2]/tbody/tr/th"))
cols = len(browser.find_elements_by_xpath("//*[@id='mw-content-text']/div[1]/table[2]/thead/tr/th"))

print(f'this table has \n{row} rows, \n{cols} columns')

# col x_path : //*[@id="mw-content-text"]/div[1]/table[2]/thead/tr/th[3]

for r in range(2, row+1):
    for c in range(1, cols+1):
        value = browser.find_element_by_xpath("//*[@id='mw-content-text']/div[1]/table[2]/tbody/tr["+str(r)+"]/th["+str(c)+"]").text
        print(value, end="  ")
    print()
# we have done type casting in above line
browser.quit()



