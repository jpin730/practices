# !/bin/bash

echo "Written with echo command" >> $1

cat << EOM >> $1
$2
EOM
