#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from faker import Faker
import random
import sys

username = str(sys.argv[1]) # value given to the script = ./freewifi <username>
fake = Faker() # to generate fake data
user_file = "wifi_users.txt" # file to read last username
logout = webdriver.Chrome("/usr/bin/chromedriver") # logout driver
login  = webdriver.Chrome("/usr/bin/chromedriver") # login  driver

# get last username from .txt file
list_names = []
with open(user_file) as f:
    for line in f:
        list_names.append(line.strip()) # saves names into file
pre_user = list_names[-1]

# DISCONNECTING FROM PREVIOS CONNECTED NETWORK
logout.get("https://wifi.superloop.com/user_status") # check account status
logout.find_elements_by_xpath("//*[@id='username']")[0].send_keys(pre_user) # login with username and password
logout.find_elements_by_xpath("//*[@id='password']")[0].send_keys(pre_user)
logout.find_elements_by_xpath("//*[@id='content']/div[2]/div/form/p/input")[0].submit() # continue
logout.find_elements_by_xpath("//*[@id='content']/div[2]/div/table[1]/tbody/tr[2]/td[3]/button")[0].click() #disconect
# LOGIN OUT
login.get("https://google.com") # login into a page to trigger automatic login
login.find_elements_by_xpath("//*[@id='old']")[0].click() # click on old
login.find_elements_by_xpath("//*[@id='username']")[0].send_keys(pre_user) # login
login.find_elements_by_xpath("//*[@id='password']")[0].send_keys(pre_user)
login.find_elements_by_xpath("//*[@id='content']/div[2]/div/form/p/input")[0].submit() # continue
login.find_elements_by_xpath("//*[@id='loginbar']/ul/li[6]/a")[0].click() # logout
# CREATE ACCOUNT
login.get("https://google.com") # trigger automatic response
login.find_elements_by_xpath("//*[@id='content']/div[2]/div/form/a")[0].click() # click on join
login.find_elements_by_xpath("//*[@id='Room']")[0].send_keys(random.randint(0,2000))  # provide room number
login.find_elements_by_xpath("//*[@id='Name']")[0].send_keys(fake.name()) # random name
login.find_elements_by_xpath("//*[@id='Mail']")[0].send_keys(username+"@gmail.com")  # email
login.find_elements_by_xpath("//*[@id='Mobile']")[0].send_keys(random.randint(0,100000000)) # random phone
login.find_elements_by_xpath("//*[@id='UserName']")[0].send_keys(username) # username
login.find_elements_by_xpath("//*[@id='content']/div[2]/div/form/table/tbody/tr[8]/td[2]/input")[0].send_keys(username) # password
login.find_elements_by_xpath("//*[@id='content']/div[2]/div/form/table/tbody/tr[10]/td[2]/input")[0].send_keys(username) # password 2x
login.find_elements_by_xpath("//*[@id='pwquestion']")[0].send_keys("Favorite building") # question
login.find_elements_by_xpath("//*[@id='pwanswer']")[0].send_keys("QMB") # answer
check = login.find_elements_by_xpath("//*[@id='content']/div[2]/div/form/table/tbody/tr[14]/td[2]/input")[0] # check terms & conditions
check.click() 
check.submit()
login.find_elements_by_xpath("/html/body/a")[0].click() # continue
login.find_elements_by_xpath("//*[@id='content']/div[2]/div/table/tbody/tr[3]/td[2]/button")[0].click() # connect

# write new username into the file
with open(user_file,"a+") as f:
    f.write("\n"+username)

# print 
print("Pre user:",pre_user)
print("New user:",username)
print("Successfully logged in to",user_file,"enjoy the WIFI!!")