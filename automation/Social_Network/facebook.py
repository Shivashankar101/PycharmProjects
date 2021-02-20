from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import datetime
import time


driver = webdriver.Safari()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(10)

try:
    driver.find_element_by_name("email").send_keys('shivashankarawati@gmail.com')
    driver.find_element_by_name("pass").send_keys('Pgpgpgagj100.')
    driver.find_element_by_name("login").click()

    time.sleep(10)
    WebDriverWait(driver, 10).until(EC.alert_is_present()).dismiss()
    #driver.find_element_by_xpath("//*[@id='mobileMirrorContent']/div/div")



    # main_frame = driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]")
    # driver.switch_to.frame(main_frame)

    upload_button = driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[3]/div/div/div/div[1]/div/div[1]/span").click()
    upload_button.send_keys("/motog4+/trip to nandi hill with vishal, dabbang, dinny/IMG_20170709_063820803.jpg")

    post_button = driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div/div[1]")
    post_button.click()
    # search_tab = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mount_0_0']/div/div[1]/div/div[2]/div[2]/div/div/div/div/label/input")))
    # search_tab.send_keys("Shravan Kalyani")
    # Shravan = driver.find_element_by_xpath("//*[@id='Shravan Kalyani_100000741597566_direct_nav_suggestion']/div/a/div/div[2]/div")
    #
    # act = ActionChains()
    # act.move_to_element(Shravan).click().perform()
    # driver.back()

except:
#    print(e)
    now = datetime.now().srtftime('%Y-%m-%d_%H-%M-%S')
    driver.get_screenshot_as_file(f"screenshot-{now}.png")

# finally:
#     time.sleep(5)
#     driver.quit()
