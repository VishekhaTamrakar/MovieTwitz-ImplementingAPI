import unittest
import time
from . import mypkg

class add_customer(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = mypkg.getOrCreateWebdriver()
        self.driver.maximize_window()

    def test_add_customer(self):
        driver = self.driver
        wait = 2
        driver.find_element_by_xpath('//*[@id="applayout"]/div/div/div/div/div/div/div/div/div[1]/div/div/p[2]/a[2]').click()
        time.sleep(wait)
        driver.find_element_by_id('id_customer_name').send_keys('John Doe')
        driver.find_element_by_id('id_organization').send_keys('ABC Company')
        driver.find_element_by_id('id_role').send_keys('Manager')
        driver.find_element_by_id('id_building_room').send_keys('ABC - 123')
        driver.find_element_by_id('id_account_number').send_keys('111')
        driver.find_element_by_id('id_address').send_keys('ABC Street')
        driver.find_element_by_id('id_city').send_keys('Omaha')
        driver.find_element_by_id('id_state').send_keys('NE')
        driver.find_element_by_id('id_zipcode').send_keys('68102')
        driver.find_element_by_id('id_email').send_keys('johndoe@test.com')
        driver.find_element_by_id('id_phone').send_keys('4021234567')
        time.sleep(wait)
        driver.find_element_by_xpath('//*[@id="applayout"]/div/div/div/div/form/button').click()
        time.sleep(wait)

#     def tearDown(self):
#         self.driver.quit()
#
# if __name__ == '__main__':
#     unittest.main()