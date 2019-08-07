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
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/a[1]').click()
        time.sleep(wait)
        driver.find_element_by_id('identifierId').send_keys('krvikash.dev@gmail.com')
        driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
        time.sleep(wait)
        driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('dev@imkv')
        driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys('Jurassic Park')
        time.sleep(wait)
        driver.find_element_by_xpath('//*[@id="movie_search_form"]/div/div[2]/button').click()
        time.sleep(wait)
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div[2]/a/img').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[1]/li[1]/a').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="navbarDropdownMenuLink"]').click()
        driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[2]/li[2]/div/a[1]').click()
