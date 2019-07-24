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
        driver.get('https://vik-8210-mfs.herokuapp.com/')
        time.sleep(wait)
        driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li[1]/a').click()
        driver.find_element_by_id('id_username').send_keys('instructor')
        driver.find_element_by_id('id_password').send_keys('instructor1a')
        driver.find_element_by_xpath('//*[@id="applayout"]/div/div/div/form/input[2]').click()
        time.sleep(wait)

#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == '__main__':
#     unittest.main()