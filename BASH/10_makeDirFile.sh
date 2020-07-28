# !/bin/bash

if [ $1 = "-d" ]; then
    mkdir -m 744 $2
    echo "Directory created."
    ls -alh $2
elif [ $1 == "-f" ]; then
    touch $2
    echo "File created."
    ls -alh $2
else
    echo "Option $1 is invalid."
fi
