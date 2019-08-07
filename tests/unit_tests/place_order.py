import unittest
import time
import random
from . import mypkg
from selenium.webdriver.support.ui import Select

class view_summary(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = mypkg.getOrCreateWebdriver()
        self.driver.maximize_window()

    def test_order(self):
        driver = self.driver
        wait = 2
        assert "Login"
        driver.get('https://movie-twizt.herokuapp.com/')
        time.sleep(wait)
        driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[2]/li[1]/a').click()
        driver.find_element_by_id('id_username').send_keys('test123')
        driver.find_element_by_id('id_password').send_keys('Test1234')
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/p/button').click()
        time.sleep(wait)
        assert "Shop Now"
        driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[1]/li[3]/a').click()
        driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/ul/li[2]').click()
        driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div[1]/a').click()
        select = Select(driver.find_element_by_id("id_quantity"))
        select.select_by_value('3')
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/div/div/form/input[3]').click()
        assert "Continue Shopping"
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/p/a[1]').click()
        driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div[2]/a').click()
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/div/div/form/input[3]').click()
        assert "Remove product"
        time.sleep(wait)
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/table/tbody/tr[2]/td[4]/a').click()
        select = Select(driver.find_element_by_id("id_quantity"))
        select.select_by_value('5')
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/table/tbody/tr[1]/td[3]/form/input[2]').click()
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/p/a[2]').click()
        driver.find_element_by_id('id_first_name').send_keys('test123')
        driver.find_element_by_id('id_last_name').send_keys('payment')
        driver.find_element_by_id('id_email').send_keys('abc@gmail.com')
        driver.find_element_by_id('id_phone').send_keys('402-777-8787')
        driver.find_element_by_id('id_address').send_keys('61 W, Dodge street,#6')
        driver.find_element_by_id('id_postal_code').send_keys('68106')
        driver.find_element_by_id('id_city').send_keys('Omaha')
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/form/p/input').click()
        time.sleep(wait)
        driver.find_element_by_xpath('//*[@id="navbarDropdownMenuLink"]').click()
        driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[2]/li[2]/div/a[2]').click()
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/table/tbody/tr[1]/td[5]/a').click()
        time.sleep(wait)
        driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[1]/li[1]/a').click()
        time.sleep(wait)
        driver.find_element_by_xpath('//*[@id="navbarDropdownMenuLink"]').click()
        driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[2]/li[2]/div/a[1]').click()
        time.sleep(wait)
