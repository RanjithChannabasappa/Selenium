# *_* coding: UTF8 *_*

"""
Selenium Practice: This script downloads latest Python3x.exe
"""

#import sys
from selenium import webdriver

DRIVER = webdriver.Chrome()
DRIVER.get("http://www.python.org")
assert "Python" in DRIVER.title
DOWN_NAVI = DRIVER.find_element_by_xpath("//*[@id='downloads']/a").click()
DOWN_EXE = DRIVER.find_element_by_xpath\
    ("//*[@id='touchnav-wrapper']/header/div/div[2]/div/div[3]/p/a").click()
assert "No results found." not in DRIVER.page_source
