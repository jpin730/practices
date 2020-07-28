# !/bin/bash

numArray=(1 2 3 4 5 6)
strArray=(abc, def, ghi, jkl)
rangeArray=({A..Z} {10..20})

echo "For in loop with numeric array:"
for num in ${numArray[*]}
do
    echo "Number: $num = ${numArray[$num-1]} "
done
echo

echo "For in loop with files:"
for f in *
do
    echo "File name: $f"
done
echo

echo "For in loop with files:"
for f in $(ls)
do
    echo "File name: $f"
done
echo

echo "Standard for loop"
for ((i=1; i<10; i++))
do
    echo $i
done
echo

echo "Standard while loop"
num=1
while [ $num -ne 10 ]
do
    echo $num
    num=$(( num + 1 ))
done
echo

echo "Numeric array items: ${numArray[*]}"
echo "Numeric array size: ${#numArray[*]}"
echo
echo "Strings array items: ${strArray[*]}"
echo "Strings array size: ${#strArray[*]}"
echo
echo "Range array items: ${rangeArray[*]}"
echo "Range array size: ${#rangeArray[*]}"
echo

numArray[5]=20
unset numArray[0]
echo "Numeric array items: ${numArray[*]}"
echo "Numeric array size: ${#numArray[*]}"
