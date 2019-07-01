#!/usr/bin/env python3

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/home/nestoregon/.config/google-chrome/")
browser = webdriver.Chrome(chrome_options=options)
browser.get("https://www.google.com/search?q=weather+forecast&oq=weather+forecast&aqs=chrome..69i57j0l5.2645j1j7&sourceid=chrome&ie=UTF-8")

# browser.get('https://www.google.co.in/')

# ChromeOptions options = new ChromeOptions();
# options.addArguments("user-data-dir=/path/to/your/custom/profile");