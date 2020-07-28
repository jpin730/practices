# !/bin/bash

host=""
user=""

read -p "Input host:" host
read -p "Input user:" user

rsync -avz $(pwd) $user@$host:/home/jaime/Downloads/
