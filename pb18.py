with open("pb18.txt","r") as file:
    a = file.read()
    b= a.splitlines()
    print(b)
    allnum= []
    for i in b:
        toadd = []
        for s in i.split():
            toadd.append(int(s))
        allnum.append(toadd)

allnum = allnum[::-1]
print(allnum)
sum = 98
current = 2
for i in allnum:
    if i[current] < i[current-1]:
        current-=1
    print(i[current])

    sum+= i[current]
    print(sum)


print(sum)