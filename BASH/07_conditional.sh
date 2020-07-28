# !/bin/bash

num=0
age=0
letter=""
option=""

read -n1 -p "Input a number (0-9): " num
echo
if (( $num > 5 )); then
    echo "Number is greater than 5."
elif [ $num -eq 5 ]; then
    echo "Number is iqual to 5."
else
    echo "Number is less than 5."
fi
echo

read -p "Input your age: " age
if [ $age -lt 10 ]; then
    echo "You are a child."
elif [ $age -ge 10 ] && [ $age -lt 18 ]; then
    echo "You are a teenager"
else
    echo "You are an adult."
fi
echo

read -n1 -p "Input a letter: " letter
echo
if [ $letter = "a" ] || [ $letter = "e" ] || [ $letter = "i" ] || [ $letter = "o" ] || [ $letter = "u" ]; then
    echo "The letter is a vowel."
else
    echo "The letter is a consonant."
fi
echo

read -n1 -p "Input a option (a-z): " option
echo
case $option in
    "a") echo "Option a.";;
    "b") echo "Option b.";;
    "c") echo "Option c.";;
    [d-z]) echo "Option d-z.";;
    *) echo "Invalid option.";;
esac
