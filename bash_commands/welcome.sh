#!/bin/bash

greeting="Welcome"
user=$(whoami)
day=$(date +%A)

echo "$greeting from $user! Today is $day, which is the best day of the entire week!"
echo "Your bash shell version is $BASH_VERSION. Enjoy!"