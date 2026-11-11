def write_to_file(c):
    fp=open("expenses.txt","w")
    for item in c:
        data=item[0]+" "+item[1]+" "+str(item[2])+"\n"
        fp.write(data)
    fp.close()
def read_data_from_file():
    ct=[]
    with open("expenses.txt") as f:
        for line in f:
            s=line.split()
            ct.append((s[0],s[1],s[2]))

    return ct
#k=read_data_from_file()
#print(k)