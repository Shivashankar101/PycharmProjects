import unittest
from selenium import webdriver

class SearchEngineTest(unittest.TestCase):

    def test_google(self):
        #self.driver = webdriver.Safari()
        self.driver = webdriver.Firefox(executable_path="/Users/shiv/Desktop/drivers/gecko/geckodriver.exe")
        self.driver.get("https://www.google.com")
        print("\nTitle of the page is :" +  self.driver.title)
        self.driver.close()

    def test_wikipedia(self):
        #self.driver = webdriver.Safari()
        self.driver = webdriver.Firefox(executable_path="/Users/shiv/Desktop/drivers/gecko/geckodriver.exe")
        self.driver.get("https://www.wikipedia.org")
        print("\nTitle of the page is :" + self.driver.title)
        self.driver.close()

    def test_bing(self):
        # self.driver = webdriver.Safari()
        self.driver = webdriver.Firefox(executable_path="/Users/shiv/Desktop/drivers/gecko/geckodriver.exe")
        self.driver.get("https://bing.com")
        print("\nTitle of the page is :" + self.driver.title)
        self.driver.close()

if __name__=="__main__":
    unittest.main()
