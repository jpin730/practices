# !/bin/bash

option=0
currentDate=`date +%Y%m%d`

# INSTALL FUNCTION

install () {
    echo "Installing..."
    echo "Verifying installation..."
    verifyInstall=$(which psql)
    if [ $? -eq 0 ]; then
        echo "Postgres is already installed."
    else
        read -s -p "Input sudo password: " sudoPassword
        echo
        read -s -p "Input Postgres password: " passwordPostgres
        echo
        echo "$sudoPassword" | sudo -S apt update
        echo "$sudoPassword" | sudo -S apt-get -y install postgresql postgresql-contrib
        sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD '{$PASSWORDPOSTGRES}';"
        echo "$sudoPassword" | sudo -S systemctl enable postgresql.service
        echo "$sudoPassword" | sudo -S systemctl start postgresql.service
    fi    
    read -n 1 -s -r -p "Press ENTER to continue..."
}

# UNINSTALL FUNCTION

uninstall () {
    read -s -p "Input sudo password: " sudoPassword
    echo "Unistalling..."
    echo -e "\n"
    echo "$sudoPassword" | sudo -S systemctl stop postgresql.service
    echo "$sudoPassword" | sudo -S apt-get -y --purge remove postgresql\*
    echo "$sudoPassword" | sudo -S rm -r /etc/postgresql
    echo "$sudoPassword" | sudo -S rm -r /etc/postgresql-common
    echo "$sudoPassword" | sudo -S rm -r /var/lib/postgresql
    echo "$sudoPassword" | sudo -S userdel -r postgres
    echo "$sudoPassword" | sudo -S groupdel postgresql
    read -n 1 -s -r -p "Press ENTER to continue..."
}

# BACKUP FUNCTION

createBackup () {
    read -s -p "Input sudo password: " sudoPassword
    echo "Databases list:"
    sudo -u postgres psql -c "\l"
    read -p "Input database name: " dbBackup
    echo
    if [ -d "$1" ]; then
        echo "Setting permissions..."
        echo "$sudoPassword" | sudo -S chmod 755 $1
        echo "Creating backup..."
        sudo -u postgres pg_dump -Fc $dbBackup > "$1/dbBackup$currentDate.bak"
        echo "Backup done in: $1/dbBackup$currentDate.bak"
    else
        echo "Directory $1 does not exist."
    fi
    read -n 1 -s -r -p "Press ENTER to continue..."
}

# RESTORE FUNCTION

restoreBackup () {
    echo "Backups list:"
    ls -1 $1/*.bak
    read -p "Input backup name: " backupToRestore
    echo
    read -p "Input detination database: " destDb
    #Verificar si la bdd existe
    verifyDb=$(sudo -u postgres psql -lqt | cut -d \| -f 1 | grep -wq $destDb)
    if [ $? -eq 0 ]; then
        echo "Restoring in destination database: $destDb"
    else
        sudo -u postgres psql -c "create database $destDb"
    fi
    if [ -f "$1/$backupToRestore" ]; then
        echo "Restoring backup..."
        sudo -u postgres pg_restore -Fc -d $destDb "$1/$backupToRestore"
        echo "Database list:"
        sudo -u postgres psql -c "\l"
    else
        echo "Backup $backupToRestore does not exist."
    fi    
    read -n 1 -s -r -p "Press ENTER to continue..."
}

# MAIN MENU

while :
do
    clear
    echo "__________________________"
    echo "POSTGRES UTILITIES PROGRAM"
    echo "__________________________"
    echo "         MAIN MENU        "
    echo "__________________________"
    echo "    1. Install."
    echo "    2. Uninstall."
    echo "    3. Create Backup."
    echo "    4. Restore Backup."
    echo "    5. Quit."
    echo "__________________________"
    echo

    read -n1 -p "Input an option (1-5): " option
    echo

    case $option in
        1)  
            install;;
        2)  
            uninstall;;
        3)  
            read -p "Input backup directory: " backupDir
            createBackup $backupDir;;
        4)  
            read -p "Input backup directory: " backupDir
            restoreBackup $backupDir;;
        5)  
            echo "Quitting..."
            sleep 2
            clear
            exit 0;;
    esac
done