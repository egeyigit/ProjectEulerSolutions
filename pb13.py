
sum =0 
with open("pb13.txt","r") as file:
    a = file.read()
    b= a.splitlines()
    print(b)
    allnum= []
    for i in b:
        toadd = []
        for s in i.split():
            toadd.append(int(s))
        allnum.append(toadd)
    print(allnum)


for i in allnum:
    sum+=i[0]
    
print(sum)