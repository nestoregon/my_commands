#!/bin/bash

function repo_remove(){
    cwd=$(pwd)
    sudo rm -r $1
    # cd ~/my_commands/python_commands
    # python3 repo_remove.py $1
    cd $cwd
}