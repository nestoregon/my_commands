#!/usr/bin/env python3

from selenium import webdriver
# from selenium import ChromeOptions
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()