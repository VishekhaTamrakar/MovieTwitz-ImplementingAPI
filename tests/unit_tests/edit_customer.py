import unittest
import time
from . import mypkg

class Test_edit_cust(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = mypkg.getOrCreateWebdriver()
        self.driver.maximize_window()

    def test_edit_customer(self):
        driver = self.driver
        wait = 2
        driver.find_element_by_xpath('//*[@id="applayout"]/div/div/div/div/div/div[3]/a[1]/span').click()
        time.sleep(wait)
        driver.find_element_by_id('id_role').clear()
        driver.find_element_by_id('id_role').send_keys('Asst Manager')
        time.sleep(wait)
        driver.find_element_by_xpath('//*[@id="applayout"]/div/div/div/div/form/button').click()
        time.sleep(wait)