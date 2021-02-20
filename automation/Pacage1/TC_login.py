import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox(executable_path="/Users/shiv/Desktop/drivers/gecko/geckodriver")
act = ActionChains(driver)


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = driver

    # @classmethod
    # def setUp(self):
    #     driver.get(url)
    #     self.assertEqual(page_title, driver.title , "page title is not matching")
    #     login_tab.send_keys(login_id).submit()
    #     password_tab.send_keys(password).submit()



    @unittest.SkipTest
    def test_by_email(self):
        try:
            url = 'https://stackoverflow.com/'
            driver.get(url)

            if driver.title == " Ask Question ":
                driver.get("https://mail.google.com")
                driver.save_screenshot('/Users/shiv/PycharmProjects/automation/screenshots/gmail3.png')

            else:
                login = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/ol[2]/li[2]/a[1]")))
                login.click()
                with_google = driver.find_element_by_xpath("//*[@id='openid-buttons']/button[1]")
                with_google.click()
                acc1 = driver.find_element_by_xpath("//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div")
                another_acc = driver.find_element_by_xpath(
                    "//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[2]/div/div/div[2]")
                login = driver.find_element_by_name("identifier")
                password = driver.find_element_by_name("password")

                if acc1.is_displayed():
                    acc1.click()
                elif another_acc.is_displayed():
                    another_acc.click()
                    login.send_keys("vishwamanava5").submit()
                    password.send_keys("Pavan@keshav").submit()
                else:
                    login.send_keys("vishwamanava5").submit()
                    password.send_keys("Pavan@keshav").submit()
                # login.click().send_keys(id)

                # user.submit()
                # time.sleep(3)
                # pw = driver.find_element(By.NAME, "password")
                # pw.send_keys(password)
                # pw.send_keys(Keys.ENTER)
                driver.get("https://mail.google.com")
                time.sleep(3)
                driver.save_screenshot('/Users/shiv/PycharmProjects/automation/screenshots/gmail4.png')
        except AttributeError:
            driver.save_screenshot('/Users/shiv/PycharmProjects/automation/screenshots/gmail_error2.png')

    # @unittest.SkipTest
    def test_by_fb(self):
        url = 'https://www.facebook.com/'
        id = 'shivashankarawati@gmail.com'
        password = 'Pgpgpgagj100.'
        driver.get(url)
        user = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.NAME, "email")))
        user.send_keys(id)
        user.send_keys(Keys.ENTER)
        time.sleep(3)
        pw = driver.find_element(By.NAME, "pass")
        pw.send_keys(password)
        pw.send_keys(Keys.ENTER)

    # @unittest.SkipTest
    def test_by_twtter(self):
        url = 'https://twitter.com/login'
        id = 'shivashankarawati@gmail.com'
        password = 'Pgpgpgagj100.'
        driver.get(url)
        user = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.NAME, "session[username_or_email]")))
        user.send_keys(id)
        # user.send_keys(Keys.ENTER)
        time.sleep(3)
        pw = driver.find_element(By.NAME, "session[password]")
        pw.send_keys(password)
        # pw.send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span").click()

    # @classmethod
    # def tearDown(self) -> None:
    #     self.driver.close()


    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(2)
        cls.driver.quit()


if __name__=="__main__":
    unittest.main()

