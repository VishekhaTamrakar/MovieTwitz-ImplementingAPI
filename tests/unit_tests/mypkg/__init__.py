from selenium import webdriver

DRIVER = None

def getOrCreateWebdriver():
    global DRIVER
    DRIVER = DRIVER or webdriver.Chrome()
    return DRIVER