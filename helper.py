expense=[]
def menu():
    print("1=> Enter Expense")
    print("2=> Display Expense")
    print("3=> Delete Expense")
    print("4=> Update Expense")
    print("Enter an operation you want to perform")
    op=int(input("Option Value"))
    return op
def enter_expense():
    description=input("Describe Expense: ")
    cost=input("Enter Expense: ")
    date=input("Enter Date: ")
    #print(name+" "+email+" "+mobile)
    expense.append((description,cost,date))
def display_expense():
    for e in expense:
                print(e[0]+" "+e[1]+" "+e[2])
def delete_expense():
    i=int(input("Enter the index you want to delete"))
    del expense[i]
def update_expense():
    i=int(input("Enter the index you want to Update"))
    description=input("Redescribe")
    cost=input("Enter New Cost")
    date=input("Enter New Date")
    expense[i]=(description,cost,date)
def get_expense():
     return expense
def set_expense(d):
     global expense
     expense=d
