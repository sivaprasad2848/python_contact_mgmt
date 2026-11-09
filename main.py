from helper import *
from fileop import *
y=0
kdata=read_data_from_file()
set_contact(kdata)
while(y==0):
    opt=menu()
    if opt==1:
        insert_contact()
    if opt==2:
        display_contact()
    if opt==3:
        delete_contact()
    if opt==4:
        update_contact()

    y=int(input("Do you want to continue?(press 0 for yes)"))
    if y!=0:
        data1=get_contact()
        write_to_file(data1)