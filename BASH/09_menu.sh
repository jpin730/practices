# !/bin/bash

option=0

while :
do
    clear
    echo "_________________________"
    echo "     Utility Program     "
    echo "_________________________"
    echo "        MAIN MANU        "
    echo "_________________________"
    echo "  1. Install."
    echo "  2. Uninstall."
    echo "  3. Create Backup."
    echo "  4. Restore Backup."
    echo "  5. Quit."
    echo "_________________________"
    echo

    read -n1 -p "Input an option (1-5): " option
    echo

    case $option in
        1)  echo "Installing..."
            sleep 3;;
        2)  echo "Unistalling..."
            sleep 3;;
        3)  echo "Creating Backup..."
            sleep 3;;
        4)  echo "Restoring Backup..."
            sleep 3;;
        5)  echo "Quitting..."
            sleep 3
            exit 0;;
    esac
done
