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
        driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[2]/li[2]/a').click()
        time.sleep(wait)
        driver.find_element_by_id('id_first_name').send_keys('test')
        driver.find_element_by_id('id_last_name').send_keys('testing')
        driver.find_element_by_id('id_username').send_keys('test' + str(random.randint(1, 100000)))
        driver.find_element_by_id('id_email').send_keys('im.kumarvikash@gmail.com')
        driver.find_element_by_id('id_password').send_keys('im.kumarvikash@gmail.com')
        time.sleep(wait + 2)
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/button').click()
        time.sleep(wait)