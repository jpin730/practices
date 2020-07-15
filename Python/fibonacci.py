def fibonacci(n):
  if n < 0:
    return 0
  elif n == 0 or n == 1:
    return 1
  return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))