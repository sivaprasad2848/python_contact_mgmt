from helper import *
from fileop import *
y=0
kdata=read_data_from_file()
set_expense(kdata)
while(y==0):
    opt=menu()
    if opt==1:
        enter_expense()
    if opt==2:
        display_expense()
    if opt==3:
        delete_expense()
    if opt==4:
        update_expense()

    y=int(input("Do you want to continue?(press 0 for yes)"))
    if y!=0:
        data1=get_expense()
        write_to_file(data1)