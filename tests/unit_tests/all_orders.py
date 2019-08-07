import unittest
import time
from . import mypkg
from selenium.webdriver.common.keys import Keys
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
        driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[1]/li[6]/a').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/table/tbody/tr/td[5]/a').click()
        elem = driver.find_element_by_xpath('//*[@id="navbarDropdownMenuLink"]')
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        elem = driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[2]/li[2]/div/a')
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
