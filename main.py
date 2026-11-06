y=0
contact=[]
while(y==0):
    print(15*"=")
    print("1=>For Insert Contact")
    print("2=>For Display Contact")
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
        print(contact)
    y=int(input("Do you want to continue?(press 0 for yes)"))