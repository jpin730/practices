number = int(input('Enter a number: '))
eps = 0.0001
step = eps**2
squareRoot = 0

while abs(squareRoot**2 - number) >= eps and squareRoot < number:
  squareRoot += step

if abs(squareRoot**2 - number) < eps:
  print(f'sqrt({number}) = {squareRoot}')
else:
  print(f'sqrt({number}) was not found.')