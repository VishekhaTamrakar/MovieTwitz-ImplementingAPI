import unittest
from unit_tests import mypkg
from unit_tests import login, signup, show_time,Global_movie_search,movie_add,all_orders,movie_edit_update,place_order,rest_movie

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.loader.findTestCases(login))
test_suite.addTest(unittest.loader.findTestCases(signup))
test_suite.addTest(unittest.loader.findTestCases(show_time))
test_suite.addTest(unittest.loader.findTestCases(Global_movie_search))
test_suite.addTest(unittest.loader.findTestCases(movie_add))
test_suite.addTest(unittest.loader.findTestCases(all_orders))
test_suite.addTest(unittest.loader.findTestCases(movie_edit_update))
test_suite.addTest(unittest.loader.findTestCases(place_order))
test_suite.addTest(unittest.loader.findTestCases(rest_movie))
# Add your individual testcases here


# Wrapping up

unittest.TextTestRunner(verbosity=2).run(test_suite)
driver = mypkg.getOrCreateWebdriver()
driver.close()