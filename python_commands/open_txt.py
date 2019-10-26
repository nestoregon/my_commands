#!/usr/bin/env python3

username = input("New user: ")

with open("wifi_users.txt","a+") as f:
    f.write("\n"+username)