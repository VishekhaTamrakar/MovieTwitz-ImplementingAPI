import unittest
import time
import random
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
        driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[1]/li[1]/a').click()
        time.sleep(wait)
        driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys('Spider')
        driver.find_element_by_xpath('//*[@id="movie_search_form"]/div/div[2]/button').click()
        time.sleep(wait)
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div[1]/a/img').click()
        time.sleep(wait + 2)
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/button').click()
        time.sleep(wait)
        driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[1]/li[1]/a').click()
        time.sleep(wait)