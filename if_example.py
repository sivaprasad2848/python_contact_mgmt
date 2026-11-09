'''This file contains basic python program example
    conditional Statements Examples

a=int(input("Enter First Number"))
b=int(input("Enter Second Number"))
#print(type(a))
print(a+b)
'''
#odd or even checking
'''
a=int(input("Enter a number"))
res=a%2
if(res==0):
    print("The number is even")
else:
    print("The number if odd")
    '''
'''
day=int(input("Enter a day"))
if day==1:
    print("Sunday")
if day==2:
    print("Monday")
if day==3:
    print("Tuesday")
if day==4:
    print("Wednesday")
if day==5:
    print("Thursday")
if day==6:
    print("Friday")
if day==7:
    print("Saturday")
if day>7 or day<1:
    print("Invalid Day")'''
'''
products=['apple','orange','mango']
for item in products:
    print(item)
'''
'''
i=0
while(i<10):
    print(i)
    i=i+1
    '''
#inner loop
'''
i=1
while i<8:
    j=1
    while j<10:
        res=i*j
        print(str(i)+"*"+str(j)+"="+str(res))
        j=j+1
    i=i+1
'''
'''
i=1
while(i<10):
    if(i==3):
        i=i+1
        #break;
        continue;
    print(i)
    i=i+1
    '''
#File Operation
# name=input("Enter your name")
# fp=open("data.txt","w")
# fp.write(name)
# fp.close()

# name=input("Enter Your Name")
# email=input("Enter Email")
# mobile=input("Enter Mobile")
# data=name+" "+email+" "+mobile
# fp=open("data.txt","w")
# fp.write(data)
# fp.close()
def write_to_file(c):
    fp=open("data.txt","a")
    for item in c:
        data=item[0]+" "+item[1]+" "+str(item[2])+"\n"
        fp.write(data)
    fp.close()
contacts=[('sam','sam@gmail.com',8728378),('thaswin','thaswin@gmail.com',800008),('rihan','rihan@gmail.com',8888888)]
write_to_file(contacts)







































