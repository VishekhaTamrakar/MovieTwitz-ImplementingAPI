import unittest
import time
from . import mypkg

class view_summary(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = mypkg.getOrCreateWebdriver()
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        wait = 2
        driver.get('https://movie-twizt.herokuapp.com/')
        time.sleep(wait)
        driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[2]/li[1]/a').click()
        time.sleep(wait)
        driver.find_element_by_id('id_username').send_keys('instructor')
        driver.find_element_by_id('id_password').send_keys('instructor1a')
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/p/button').click()
        time.sleep(wait)
        driver.find_element_by_xpath('//*[@id="navbarDropdownMenuLink"]').click()
        driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[2]/li[2]/div/a').click()