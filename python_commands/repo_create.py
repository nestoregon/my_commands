#!/usr/bin/env python3

import sys
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/home/nestoregon/.config/google-chrome/")
browser = webdriver.Chrome(chrome_options=options)

def repo_create():
    # Obtain folder name from input 
    folder_name = str(sys.argv[1])

    # Go to new repository
    browser.get('https://github.com/new')

    # name the repository
    python_button = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]
    python_button.send_keys(folder_name) 

    # create repository
    python_button = browser.find_elements_by_xpath("//*[@id='new_repository']/div[3]/button")[0]
    python_button.submit() #click() didn't work here so submit() instead
    browser.click() # really important, without this it won't continue
    

if __name__ == "__main__":
    repo_create()