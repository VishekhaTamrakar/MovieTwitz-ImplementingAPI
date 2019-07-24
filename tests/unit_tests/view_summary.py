import unittest
import time
from . import mypkg

class view_summary(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = mypkg.getOrCreateWebdriver()
        self.driver.maximize_window()

    def test_view_summary(self):
        driver = self.driver
        wait = 2
        # driver.get('https://vik-8210-mfs.herokuapp.com/')
        driver.find_element_by_xpath('//*[@id="applayout"]/div/div/div/div/div/div[3]/a[2]/span').click()
        time.sleep(wait)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(wait)

    def tearDown(self):
        self.driver.close()
#
# if __name__ == '__main__':
#     unittest.main()