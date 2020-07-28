# !/bin/bash

echo "Reading with cat."
cat $1
echo

echo "Reading with command substitution of cat."
valueCat=`cat $1`
echo "$valueCat"
echo

# IFS (Internal Field Separator) para evitar que los espacios en blanco al inicio al final se recortan
echo "Reading line by line with IFS."
while IFS= read line
do
    echo "$line"
done < $1
