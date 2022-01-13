import func

# Functions needed in this module 

Break = 1
def EndLoopFunc():
  global Break #Break var4 is out of func scope w/o Global keyword
  while True: 
        try:
          Cont = int(input("Enter 1 to conduct another transaction, enter 2 to quit: "))
          if Cont == 1:
            break
          else:
            print("saving input to tranasctions.csv file...\n")
            Break = 0
            break
        except (ValueError, func.InputNotInRangeError):
          print("Please only enter an interger from 1-2\n")

# MAIN WHILE LOOP; BREAKS WHEN INPUT IS COMPLETE (make Break = 0)
while Break:

  # DETERMINE IF THE INPUT IS A INCOME OR EXPENSE
  while True:
    try:
      Response = int(input('Are you entering an income (1) or expense (2): '))
      if not 0 < Response <= 2:
        raise func.InputNotInRangeError(Response)
      break
    except (ValueError, func.InputNotInRangeError):
        print("Please only enter 1 or 2")

  # IF INPUT IS AN INCOME 
  if Response == 1: 
    # Exception handling ensuring numeric value (float)
    while True:
      try:
        Expenses = float(input("Enter income amount in USD: "))
        break
      except ValueError:
        print("Please only enter numeric values\n")

    # Exception handling ensuring numeric value and between 1-4
    print("1. Salary\n2. Interest\n3. Tax Return\n4. Side Hustle\n")
    while True: 
      try:
        category = int(input("Enter the number that corresponds to the income category: "))
        func.InputNotInRange(category, 1, 4)
        # if not 0 < category < 5:
        #   raise InputNotInRangeError(Response)
        break
      except (ValueError, func.InputNotInRangeError):
        print("Please only enter an interger from 1-4\n")

    # Runs func to get user input; either breaks or cont main while loop 
    EndLoopFunc()


  # IF INPUT IS AN EXPENSE
  else:
    # Exception handling ensuring numeric value (float)
    while True:
      try:
        Expenses = float(input("Enter an expense amount in USD: "))
        break
      except ValueError:
        print("Please only enter numeric values\n")


    # Exception handling ensuring numeric value and between 1-10
    print("1. Housing\n2. Transportation\n3. Food\n4. Utilities\n5. Insurance\n6. Healthcare\n7. Investing\n8. Personal\n9. Recreation\n10.Savings\n")
    while True:
      try:
        category = int(input("Enter the number that corresponds to the expense category: "))
        func.InputNotInRange(category, 1, 10)
        break
      except (ValueError, func.InputNotInRangeError):
        print("Please only enter an interger from 1-10\n")

    EndLoopFunc()