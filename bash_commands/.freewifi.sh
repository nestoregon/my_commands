#!/bin/bash

function freewifi(){
    cwd=$(pwd)
    cd ~/projects/my_commands/python_commands
    ./freewifi.py $1
    cd $cwd
}