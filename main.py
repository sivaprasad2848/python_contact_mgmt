y=0
contact=[]
while(y==0):
    print(15*"=")
    print("1=>For Insert Contact")
    print("2=>For Display Contact")
    print("3=>For Delete Contact")
    print("4=>For Update Contact")
    print("Enter an operation you want to perform")
    opt=int(input("Option Value"))
    print(15*"=")
    if opt==1:
        name=input("Enter Name")
        email=input("Enter Email")
        mobile=input("Enter Mobile")
        #print(name+" "+email+" "+mobile)
        contact.append((name,email,mobile))
    if opt==2:
<<<<<<< Updated upstream
        for contactid in contact:
            print(contactid)
    if opt==3:
        print("Delete")
    if opt==4:
        print("Update")
=======
        print(contact)
        
>>>>>>> Stashed changes
    y=int(input("Do you want to continue?(press 0 for yes)"))