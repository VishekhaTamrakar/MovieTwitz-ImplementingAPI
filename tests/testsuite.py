import unittest
from unit_tests import mypkg
from unit_tests import login, add_customer, view_summary, edit_customer, delete_customer, test_login_logout

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.loader.findTestCases(test_login_logout))
# test_suite.addTest(unittest.loader.findTestCases(login))
# test_suite.addTest(unittest.loader.findTestCases(add_customer))
# test_suite.addTest(unittest.loader.findTestCases(edit_customer))
# test_suite.addTest(unittest.loader.findTestCases(delete_customer))
# test_suite.addTest(unittest.loader.findTestCases(view_summary))

unittest.TextTestRunner(verbosity=2).run(test_suite)
driver = mypkg.getOrCreateWebdriver()
driver.close()