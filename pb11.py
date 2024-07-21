


with open("pb11.txt","r") as file:
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
checklist = 
for b in allnum:
    for i, value in enumerate(b):
        currentvalues = []