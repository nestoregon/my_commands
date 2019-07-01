#!/usr/bin/env python3

import sys
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/home/nestoregon/.config/google-chrome/")
browser = webdriver.Chrome(chrome_options=options)

def repo_remove():
    # Obtain folder name from input 
    folder_name = str(sys.argv[1])
    
    # to get repository path
    repository_path = "https://github.com/nestoregon/" + folder_name + "/settings"
    browser.get(repository_path)

    python_button = browser.find_elements_by_xpath("//*[@id='options_bucket']/div[9]/ul/li[4]/details/summary")[0]
    python_button.click() # to click somewhere

    python_button = browser.find_elements_by_xpath("//*[@id='rename-field']")[0]
    python_button.send_keys(folder_name)

    python_button = browser.find_elements_by_xpath("//*[@id='options_bucket']/div[9]/ul/li[4]/details/summary")[0]
    python_button.click()
    browser.quit()

if __name__ == "__main__":
    repo_remove()