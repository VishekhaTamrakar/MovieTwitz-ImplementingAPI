import unittest
from unit_tests import mypkg
from unit_tests import login, signup, movie_search, show_time

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.loader.findTestCases(login))
test_suite.addTest(unittest.loader.findTestCases(signup))
test_suite.addTest(unittest.loader.findTestCases(movie_search))
test_suite.addTest(unittest.loader.findTestCases(show_time))
# Add your individual testcases here


# Wrapping up

unittest.TextTestRunner(verbosity=2).run(test_suite)
driver = mypkg.getOrCreateWebdriver()
driver.close()