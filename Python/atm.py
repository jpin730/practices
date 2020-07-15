# LIBRARIES
import os

# FUNCTIONS
def login():
  print('WELCOME TO THE BANK ATM\n')
  user = input('User: ')
  pssw = input('Password: ')
  if user == "jaime" and pssw == "123":
    return True
  return False

def menu(bal):
  print('BANK ATM\n\nYour balance is: $%8.2f\n' % bal)
  print('MENU:\n1. Withdraw money.\n2. Deposit money.\n3. Logout.')
  opt = int(input('\nEnter your option: '))
  return opt

def withdraw(bal):
  print('\nWITHDRAW:\n')
  amount = float(input('Enter the amount: $'))
  if amount < bal and amount > 0:
    bal -= amount
    print("\nSUCCESSFUL OPERATION")
    input('\nYour balance is: $%8.2f (Press ENTER to continue)' % bal)
    return bal
  input("\nINVALID AMOUNT (Press ENTER to continue)")
  return bal

def deposit(bal):
  print('\nDEPOSIT:\n')
  amount = float(input('Enter the amount: $'))
  if amount > 0:
    bal += amount
    print("\nSUCCESSFUL OPERATION")
    input('\nYour balance is: $%8.2f (Press ENTER to continue)' % bal)
    return bal
  input("\nINVALID AMOUNT (Press ENTER to continue)")
  return bal

# Clear screen function
cls = lambda: os.system('clear')

# VARIABLES
opt = 0
bal = 1000
log = False

# MAIN
while not log:
  cls()
  log = login()
  if log:
    while opt != 3:
      cls()
      opt = menu(bal)
      if opt == 1:
        bal = withdraw(bal)
      elif opt == 2:
        bal = deposit(bal)
      elif opt == 3:
        input("\nLOGGED OUT DONE (Press ENTER to continue)")
      else:
        input("\nERROR: Invalid Option (Press ENTER to try again)")
  else:
    input("\nWRONG INFORMATION (Press ENTER to try again)")
  log = False
  opt = 0