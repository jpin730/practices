# LIBRARIES
import os

# FUNCTIONS

# Clear screen function
cls = lambda: os.system('clear')

# Show main menu and tasks if not empty
def showMenu(xList):
  if not emptyList(xList):
    showTasks(xList)
  print('\nMENU:')
  print('1. Add task.')
  print('2. Edit task.')
  print('3. Mark/Unmark task.')
  print('4. Delete task.')
  print('5. Quit.\n')

# Is xlist is empty?
def emptyList(xList):
  if not xList:
    print('THE TASK LIST IS EMPTY')
    return True
  return False

# Show tasks
def showTasks(xList):
  print('THINGS TO DO')
  print('No. %s %-7s %s'%('Done', 'Date', 'Name'))
  for i in range(0,len(xList),3):
    if xList[i]:
      mark = '[X]'
    else:
      mark = '[ ]'
    print('%2d. %s  %-7s %s'%(i/3+1,mark,xList[i+1],xList[i+2]))

# Add task to list
def add(xList):
  print()
  xList.append(False)
  xList.append(input('Input task date: '))
  xList.append(input('Input task name: '))
  return xList

# Edit task in list
def edit(xList):
  if not emptyList(xList):
    index = whichTask(xList)
    print('\nEMPTY new name or new date will not be edited.')
    newDate = input('New date: ')
    newName = input('New name: ')
    if newDate:
      xList[index+1] = newDate
    if newName:
      xList[index+2] = newName
    return xList
  input()
  return xList

# Select which task in list
def whichTask(xList):
  while True:
    print()
    taskSelected = int(input('Input task number: '))
    if taskSelected >= 1 and taskSelected <= len(xList)/3:
      return (taskSelected - 1) * 3
    print('TASK NOT EXISTS. Try again.')

# Mark or Delete task in list
def markDel(xList, mark):
  if not emptyList(xList):
    index = whichTask(xList)
    if mark:
      xList[index] = not xList[index]
    else:
      del xList[index:index+3]
    return xList
  input()
  return xList    

# VARIABLES
task = []
opt = []

# MAIN
while opt != 5:
  cls()
  showMenu(task)
  opt = int(input('Input option: '))
  if opt == 1:
    task = add(task)
  elif opt == 2:
    task = edit(task)
  elif opt == 3 or opt == 4:
    task == markDel(task, opt == 3)
  elif opt == 5:
    input("TASKS SAVED (Press ENTER to continue)")
  else:
    input("ERROR: Invalid Option (Press ENTER to try again)")