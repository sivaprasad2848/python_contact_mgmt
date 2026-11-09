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
i=1
while(i<10):
    if(i==3):
        i=i+1
        #break;
        continue;
    print(i)
    i=i+1























