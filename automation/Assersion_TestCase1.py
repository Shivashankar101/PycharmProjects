import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    def test_Name(self):
        driver = webdriver.Firefox(executable_path="/Users/shiv/Desktop/drivers/gecko/geckodriver.exe")
        self.assertIsNotNone(driver)  # this is for checking whether value is None or Not
        driver.get("https://www.google.com")
        name = driver.title
        #self.assertEqual("Google", name, "webpage is not Google")
        #self.assertNotEqual("Wiki", name, "webpage is Google") # we can use either of them
        #self.assertTrue(name == "Google")
        self.assertFalse(name == "Wiki", msg="this is Google") # we can give conditions in ()
        driver.quit()

    #self.assertIn() #
    #self.assertNotIn() #
    # These two can be used to verify presence of certain value in tuple, set or Dict

    def test_presence(self):
        mylist = [1, 2, 3, 4, 5]
        self.assertIn(2, mylist)
        self.assertNotIn(7, mylist)

    def test_relations(self):
        a = 100
        b = 99
        self.assertGreater(a, b)
        self.assertGreaterEqual(a, b)
        self.assertNotAlmostEqual(a, b)
        # self.assertAlmostEqual(a, b)
        # self.assertLess(a, b)
        # self.assertLessEqual(a, b)



if __name__ == '__main__':
    unittest.main()