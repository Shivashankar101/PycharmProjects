import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Firefox(executable_path="/Users/shiv/Desktop/drivers/gecko/geckodriver")
act = ActionChains(driver)



def go_login_page(gmail):
    driver.implicitly_wait(30)
    driver.get(gmail)
    driver.maximize_window()

def login(id, password):

    user = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.NAME, "identifier")))
    user.send_keys(id)
    user.send_keys(Keys.ENTER)
    pw = driver.find_element(By.NAME, "password")
    pw.send_keys(password)
    pw.send_keys(Keys.ENTER)

def pop_up():
    apps = driver.find_element_by_xpath("//*[@id='gbwa']/div/a/svg")
    # apps.click()
    # apps_frame = driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/ul[1]")
    # driver.switch_to_frame(apps_frame)
    Gmail = driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/ul[1]/li[7]/a/div[5]/span")
    # driver.execute_script("arguments[0].scrollIntoView();", Gmail)
    act.move_to_element(apps).click().move_to_element(Gmail).click().perform()

def delete(name):
    search = driver.find_element_by_name('q')
    search.send_keys(name).send_keys(Keys.ENTER)

    # mail_frame  = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]")
    # driver.switch_to_frame(mail_frame)

    select = driver.find_element_by_xpath("//*[@id=':lu']/div[1]/span")
    select.send_keys(Keys.ENTER)

    delete = driver.find_element_by_xpath("//*[@id=':4']/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div")
    delete.click()

    # inbox_frame = driver.find_element_by_xpath("//*[@id=':k1']/div[1]/div")
    # driver.switch_to_frame(inbox_frame)

    inbox = driver.find_element_by_xpath("//*[@id=':kd']/div/div[2]")
    inbox.click()


def log_out():
    account = driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div[1]/div[2]/div/a/img")
    account.click()

    # acc_frame  = driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[4]")
    # driver.switch_to_frame(acc_frame)
    sign_out = driver.find_element_by_id("gb_71")
    driver.execute_script("arguments[0].scrollIntoView();", sign_out)
    sign_out.click()
    driver.quit()

class Test(unittest.TestCase):

    def test_delete_mails(name):
        # page urls
        gmail = 'https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin'
        # twitter = ' '

        # login details
        id = 'shivashankarawati@gmail.com'
        password = 'bel@1234'

        go_login_page(gmail)
        login(id, password)
        try:
            pop_up()
        except AttributeError:
            return
        delete(name)
        log_out()

if __name__=="__main__":
    unittest.main()





# def setUpModule():
#
# def tearDownModule():
#     print("\nEND : this executes one time, and after executing class, and it has to be defined outside the class")
#
# class SearchEngineTest(unittest.TestCase):
#
#     #@unittest.SkipTest # -----> # we can skip this test by using this decorator
#     def test_google(self):
#         #self.driver = webdriver.Safari()
#         self.driver = webdriver.Firefox(executable_path="/Users/shiv/Desktop/drivers/gecko/geckodriver.exe")
#         self.driver.get("https://www.google.com")
#         print("\nTitle of the page is :" +  self.driver.title)
#         self.driver.close()
#
#     #@unittest.skipIf(1==1, 'skipping for demo')
#     #@unittest.skip('skipping for demo') # we can also use this to skip a method with a reason
#     def test_wikipedia(self):
#         #self.driver = webdriver.Safari()
#         self.driver = webdriver.Firefox(executable_path="/Users/shiv/Desktop/drivers/gecko/geckodriver.exe")
#         self.driver.get("https://www.wikipedia.org")
#         print("\nTitle of the page is :" + self.driver.title)
#         self.driver.close()
#
#     def test_bing(self):
#         # self.driver = webdriver.Safari()
#         self.driver = webdriver.Firefox(executable_path="/Users/shiv/Desktop/drivers/gecko/geckodriver.exe")
#         self.driver.get("https://bing.com")
#         print("\nTitle of the page is :" + self.driver.title)
#         self.driver.close()
#
#     @classmethod
#     def setUp(self) -> None: # we use @pytest.fixture() and @pytest.yield_fixture in pytest
#         print("\nthis will run before every test")
#
#     @classmethod
#     def tearDown(self) -> None: # we use @pytest.fixture() and @pytest.yield_fixture in pytest
#         print("\nthis will run after every test")
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         print("\nStart (this will executed at the beginning of the all methods)")
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         print("\nEnd (this will executed at the end of the all methods)")
#
# if __name__=="__main__":
#     unittest.main()

