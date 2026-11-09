y=0
contact=[]
def menu():
    print("1=>For Insert Contact")
    print("2=>For Display Contact")
    print("3=>For Delete Contact")
    print("4=>For Update Contact")
    print("Enter an operation you want to perform")
    op=int(input("Option Value"))
    return op
def insert_contact():
    name=input("Enter Name")
    email=input("Enter Email")
    mobile=input("Enter Mobile")
    #print(name+" "+email+" "+mobile)
    contact.append((name,email,mobile))
def display_contact():
    for contacts in contact:
                print(contacts[0]+" "+contacts[1]+" "+contacts[2])
def delete_contact():
    i=int(input("Enter the index you want to delete"))
    del contact[i]
def update_contact():
    i=int(input("Enter the index you want to Update"))
    name=input("Enter Name")
    email=input("Enter Email")
    mobile=input("Enter Mobile")
    contact[i]=(name,email,mobile)
     
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