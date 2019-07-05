#!/bin/bash

function repo_create(){
    cwd=$(pwd)
    mkdir $1
    cd ~/my_commands/python_commands
    python3 repo_create.py $1
    cd $cwd/$1
    git init
    git remote add origin git@github.com:nestoregon/$1.git
    touch README.md
    touch .gitignore
    echo "/build/" >> .gitignore
    echo "/devel/" >> .gitignore
    git add .
    git commit -m "Initializing repository $1"
    git push -u origin master
    code .
}

# source ~/.my_commands.sh