number = int(input('Enter a number: '))
eps = 0.0001
lowLimit = 0
highLimit = max(1.0, number) # sqrt of numbers < 1 are greater than 1
squareRoot = (lowLimit + highLimit)/2

if number >= 1:
  while abs(squareRoot**2 - number) >= eps:
    if squareRoot**2 > number:
      highLimit = squareRoot
    else:
      lowLimit = squareRoot
    squareRoot = (lowLimit + highLimit)/2
  print(f'sqrt({number}) = {squareRoot}')
else:
  print(f'sqrt({number}) was not found.')