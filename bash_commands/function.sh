#!/bin/bash

function user_details {
    echo "This are the details of the user"
    echo "Username: $(whoami)"
    echo "Home directory: $HOME"
}

user_details