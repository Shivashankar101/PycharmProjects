import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import XLUtils as xl


driver = webdriver.Firefox(executable_path="/Users/shiv/Desktop/drivers/gecko/geckodriver")
act = ActionChains(driver)


xl_sheet_path = '/Users/shiv/Desktop/logindata.xlsx'
url = xl.read_data(xl_sheet_path, 'sheet1', row=1, col=2)
rows = xl.count_rows(xl_sheet_path, 'sheet1')
cols = xl.count_clos(xl_sheet_path, 'sheet1')


class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = driver

    def setUp(self):
        driver.get(url)
        driver.implicitly_wait(50)


    def test_fb(self):
        

        for r in range(2, rows + 1):
            try:
                page_title = xl.read_data(xl_sheet_path, 'sheet1', row=r, col=3)
                login_id = xl.read_data(xl_sheet_path, 'sheet1', row=r, col=4)
                password = xl.read_data(xl_sheet_path, 'sheet1', row=r, col=5)
                self.assertEqual(page_title, driver.title, "page title is not matching")
                user = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.NAME, "email")))
                user.send_keys(login_id).submit()
                pw = driver.find_element(By.NAME, "pass")
                pw.send_keys(password).submit()
                driver.save_screenshot("/Users/shiv/PycharmProjects/automation/screenshots/row{}.png".format(r))
                # xl.write_data(xl_sheet_path, sheet1, row=r, col=5, test_result)
                # xl.write_data(xl_sheet_path, sheet1, row=r, col=6, Error_message)
                # xl.write_data(xl_sheet_path, sheet1, row=r, col=7, screen_shot)

            except:
                driver.save_screenshot("/Users/shiv/PycharmProjects/automation/screenshots/Error{}.png".format(r))

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(2)
        driver.quit()


if __name__=="__main__":
    unittest.main()

