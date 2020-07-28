# !/bin/bash

numA=10
numB=4

echo -e "Numbers: A=$numA and B=$numB\n"

echo "A + B =" $((numA + numB))
echo "A - B =" $((numA - numB))
echo "A * B =" $((numA * numB))
echo "A / B =" $((numA / numB))
echo -e "A % B =" $((numA % numB)) "\n"

echo "A < B =" $((numA < numB))
echo "A > B =" $((numA > numB))
echo "A <= B =" $((numA <= numB))
echo "A >= B =" $((numA >= numB))
echo "A == B =" $((numA == numB))
echo -e "A != B =" $((numA != numB)) "\n"

echo "A += B =" $((numA += numB))
echo "A -= B =" $((numA -= numB))
echo "A *= B =" $((numA *= numB))
echo "A /= B =" $((numA /= numB))
echo "A %= B =" $((numA %= numB))
