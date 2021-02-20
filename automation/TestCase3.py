import unittest
from selenium import webdriver

def setUpModule():
    print("\nSTART : this executes one time, and before executing class, and it has to be defined outside the class")
def tearDownModule():
    print("\nEND : this executes one time, and after executing class, and it has to be defined outside the class")

class SearchEngineTest(unittest.TestCase):

    @unittest.SkipTest # -----> # we can skip this test by using this decorator
    def test_google(self):
        #self.driver = webdriver.Safari()
        self.driver = webdriver.Firefox(executable_path="/Users/shiv/Desktop/drivers/gecko/geckodriver.exe")
        self.driver.get("https://www.google.com")
        print("\nTitle of the page is :" +  self.driver.title)
        self.driver.close()

    @unittest.skipIf(1==1, 'skipping for demo')
    #@unittest.skip('skipping for demo') # we can also use this to skip a method with a reason
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

    @classmethod
    def setUp(self) -> None: # we use @pytest.fixture() and @pytest.yield_fixture in pytest
        print("\nthis will run before every test")

    @classmethod
    def tearDown(self) -> None: # we use @pytest.fixture() and @pytest.yield_fixture in pytest
        print("\nthis will run after every test")

    @classmethod
    def setUpClass(cls) -> None:
        print("\nStart (this will executed at the beginning of the all methods)")

    @classmethod
    def tearDownClass(cls) -> None:
        print("\nEnd (this will executed at the end of the all methods)")

if __name__=="__main__":
    unittest.main()
