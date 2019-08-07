import unittest
import time
import random
from . import mypkg

class view_summary(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = mypkg.getOrCreateWebdriver()
        self.driver.maximize_window()

    def test_rest(self):
        driver = self.driver
        wait = 2
        driver.get('http://movie-twizt.herokuapp.com/api/movies/')
        time.sleep(wait)
        driver.get('http://movie-twizt.herokuapp.com/api/movies/tt6105098')
        time.sleep(wait)