# !/bin/bash

option=0
backuName=""
password=""

read -n1 -p "Input an option: " option
echo
read -n10 -p "Input backup file name: " backupName
echo
echo "Option: $option, Backup Name: $backupName"

read -s -p "Input password: " password
echo -e "\nPassword: $password"
