import unittest
from unit_tests import mypkg
from unit_tests import login, signup

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.loader.findTestCases(login))
test_suite.addTest(unittest.loader.findTestCases(signup))
# Add your individual testcases here


# Wrapping up

unittest.TextTestRunner(verbosity=2).run(test_suite)
driver = mypkg.getOrCreateWebdriver()
driver.close()