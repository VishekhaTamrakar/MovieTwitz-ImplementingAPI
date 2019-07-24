#from django.test import TestCase
import unittest
import time
from . import mypkg


class Blog_ATS(unittest.TestCase):

    def setUp(self):
            #self.driver = webdriver.Chrome()
            self.driver = mypkg.getOrCreateWebdriver()
            self.driver.maximize_window()

    def test_blog(self):
        print('Attempting Test Run')
        id_user = "instructor"
        id_pwd = "instructor1a"
        driver = self.driver
        driver.get("https://movie-twizt.herokuapp.com/")
        time.sleep(2)
        elem = driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[2]/li[1]/a').click()
        time.sleep(2)
        assert "Login"
        print('Attempting authentication')
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(id_user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(id_pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "Logout"
        elem = driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[2]/li/div/a[1]').click()
        time.sleep(2)


#     def tearDown(self):
#             self.driver.close()

# if __name__ == "__main__":
#     print('Starting Test')
#     unittest.main()

# Create your tests here.
