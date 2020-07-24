from account import Account
from car import Car

if __name__ == "__main__":
  car = Car("AMS234", Account("Andres Herrera", "AND876"))
  print(vars(car))
  print(vars(car.driver))