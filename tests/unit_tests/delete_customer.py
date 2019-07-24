import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from . import mypkg

class Test_del_cust(unittest.TestCase):

   def setUp(self):
       # self.driver = webdriver.Chrome()
       self.driver = mypkg.getOrCreateWebdriver()
       self.driver.maximize_window()

   def test_delete_customer(self):

       driver = self.driver
       wait = 2
       # click delete
       time.sleep(wait)
       driver.find_element_by_xpath('//*[@id="applayout"]/div/div/div/div/div/div[3]/a[3]/span').click()
       time.sleep(wait)
       alert = driver.switch_to_alert()
       alert.accept()
       time.sleep(wait)

