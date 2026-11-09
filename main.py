from helper import *
y=0
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