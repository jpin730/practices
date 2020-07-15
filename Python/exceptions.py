def divideElementsFromList(inputList, divisor):
  try:
    return [i/divisor for i in inputList]
  except ZeroDivisionError as error:
    print(error)
    return inputList

inputList = list(range(10))
divisor = 0

print(divideElementsFromList(inputList, divisor))