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
        for contacts in contact:
            print(contacts[0]+" "+contacts[1]+" "+contacts[2])
    if opt==3:
        i=int(input("Enter the index you want to delete"))
        del contact[i]
    if opt==4:
        i=int(input("Enter the index you want to Update"))
        name=input("Enter Name")
        email=input("Enter Email")
        mobile=input("Enter Mobile")
        contact[i]=(name,email,mobile)

    y=int(input("Do you want to continue?(press 0 for yes)"))