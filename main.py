y=0
contact=[]
while(y==0):
    name=input("Enter Name")
    email=input("Enter Email")
    mobile=input("Enter Mobile")
    #print(name+" "+email+" "+mobile)
    contact.append((name,email,mobile))
    print(contact)
    y=int(input("Do you want to continue?(press 0 for yes)"))