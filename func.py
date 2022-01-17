import csv
from dataclasses import field
import shutil
from tempfile import NamedTemporaryFile


class InputNotInRangeError(Exception):
    """Exception raised for numbers out of range

    Attributes:
        number -- input number which caused the error
        message -- explanation of the error
    """

    def __init__(self, number, message="Number is not in range"):
        self.number = number
        self.message = message
        super().__init__(self.message)


def InputNotInRange(input, lower, upper):
  if not lower <= input <= upper:
    raise InputNotInRangeError(input)


def PrintDictValues(dict):
  i = 0 
  for keys in dict:
    print(list(dict.keys())[i], list(dict.values())[i])
    i += 1
  print()


def DoubleCheck(Dict, RangeMin, RangeMax):
  while True:
    category = int(input("Enter the number that corresponds to the income category: "))
    print()
    InputNotInRange(category, RangeMin, RangeMax)
    In_DubChck = input("Is {} correct? (Y/N): ".format(Dict.get(category)))
    if In_DubChck.upper() == "Y":
      return Dict.get(category)
      break
    elif In_DubChck.upper() == "N":
      print()
    else:
      print("Invalid input...Please choose again...\n")

# GET LENGTH OF CSV FILE FOR INDEXING
def get_length(file_path):
    with open(file_path) as f:
        reader = csv.reader(f)
        reader_list = list(reader)
        return len(reader_list)

# CREATE AND THEN APPEND DATA TO THE END OF A CSV FILE
def append_data(file_path, date, Transaction_Type, Description, Amount):
    fieldNames = ['id','Date', 'Transaction Type', 'Description', 'Amount']
    next_id = get_length(file_path)

    #Creates Transactions.csv if it is not created yet (first time running code)
    with open(file_path, 'a') as f:
        writer = csv.DictWriter(f, fieldnames=fieldNames)

        if f.tell() ==0:
          writer.writeheader() #-- only run this line once to add CSV headings only once
        writer.writerow({
            'id': next_id,
            'Date': date,
            'Transaction Type': Transaction_Type,
            'Description': Description,
            'Amount': Amount
        })

#append_data('Transactions.csv', '10-2-2010', 'income', 'salary', '1000')


# EDIT CSV FILE ROW BASED ON INDEX
def edit_data(file_path, edit_id, Edit_Transaction_Type, Edit_Description, Edit_Amount):
    temp_f = NamedTemporaryFile(mode="w",newline= '', delete=False)

    with open(file_path, "r") as f, temp_f:
        reader =  csv.DictReader(f)
        fieldnames = ['id','Date', 'Transaction Type', 'Description', 'Amount']
        writer = csv.DictWriter(temp_f, fieldnames = fieldnames)
        writer.writeheader()
        for row in reader:
            if int(row['id']) == int(edit_id):
                row['Transaction Type'] = Edit_Transaction_Type
                row['Description'] =  Edit_Description
                row['Amount'] = Edit_Amount

            writer.writerow(row)

    shutil.move(temp_f.name, file_path)
    return True 

    return False


#edit_data('Transactions.csv', edit_id=1, Edit_Transaction_Type = "expense", Edit_Description = "health", Edit_Amount=1000)






