#!/bin/bash

# compile and flash the given .ino file into particle electron
# .ino -> .bin
# .bin -> flash to device
# <working_dir>/<code><flash>
function pcomp(){
    file_ino=$1
    file="${file_ino%.*}"
    file_bin=$file.bin

    echo "NOTE: dir structure <working_dir>/<code><flash> "; cd ..

    particle compile electron code/$file_ino --saveTo flash/$file_bin

    echo; echo "Compilation completed. Saved in flash/$file_bin"; echo "Ready to flash ..."
    # particle flash --usb flash/$file_bin
    cd code
    echo -$file_ino C++ code  
    echo -$file_bin binary
}
