
before = 0
last = 1
allnum = [1]
numbers = []
sum = 0
indexes = []
while last < (10**1001):
    
    last = before + last
    
    before = last - before
    if len(str(before)) < len(str(last)):
        numbers.append(last)
    
    allnum.append(last)
    




for i in numbers:
    indexes.append(allnum.index(i)+1)

print(indexes)






print(indexes[998])


    
