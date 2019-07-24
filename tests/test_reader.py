import unittest
import time
import csv
from selenium import webdriver

# File to read data from
FILENAME = "products.csv"

def read_content():
    products = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            products.append(row)
    return products


# function to open add customer page to add customer details.
def addProducts(driver):
    products = read_content()  # read the content from csv file
    print(products)
    for i in range(len(products)):  # iterate the adding operation for records present in csv files
        print('Range of loop -', len(products))
        product = products[i]
        if i != 0:  # ignore the header in csv file
            # Click on Add Product
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="applayout"]/div/div/div/div/div[1]/h2/a').click()
            #Add data to form
            print('>>Value of i', i)
            driver.find_element_by_id('id_customer_name').send_keys(product[0])
            driver.find_element_by_id('id_product').send_keys(product[1])
            driver.find_element_by_id('id_product_description').send_keys(product[2])
            driver.find_element_by_id('id_quantity').send_keys(product[3])
            driver.find_element_by_id('id_charge').send_keys(product[4])
            print('Added all data')
            #Save Product
            driver.find_element_by_xpath('//*[@id="applayout"]/div/div/div/form/button').click()
            time.sleep(2)


class MFS_reader_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        wait = 2
        driver = self.driver
        driver.maximize_window()
        driver.get('https://vik-8210-mfs.herokuapp.com/')
        time.sleep(wait)
        driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li[1]/a').click()
        driver.find_element_by_id('id_username').send_keys('instructor')
        driver.find_element_by_id('id_password').send_keys('instructor1a')
        driver.find_element_by_xpath('//*[@id="applayout"]/div/div/div/form/input[2]').click()
        time.sleep(wait)

        #Click on View Products
        driver.find_element_by_xpath('//*[@id="applayout"]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/p[2]/a[1]').click()
        addProducts(driver)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
