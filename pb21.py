primes = [2]
import math
from itertools import combinations

for i in range(3,2*10**4,2):
    
    isprime= True
    for each in primes:
        if i%each==0:
            isprime = False
        if each > math.sqrt(i):
            break
    
    if isprime == True:
        primes.append(i)

def primefactor(a):
    global primes
    factorset = []
    index = -1
    for i in primes:
        index+=1
        if primes[index] > i:
            print("hey")
            break
    indexbegin = index
    
    b = a
    while b > 1:
        
        if b%primes[index]== 0:
            factorset.append(primes[index])
            b = b/primes[index]
        index-=1
        if index==-1:
            index = indexbegin

    return(factorset)

def unique(a):
    toreturn = []
    for i in a:
        if i not in toreturn:
            toreturn.append(i)
    return(toreturn)

validnumbers = []
print(primefactor(20))
print("hey")
for i in range(10000):
    a = primefactor(i)
    uniq = unique(a)
    counteach = []
    sumoffactor = 1
    for o in uniq:
        counteach.append(a.count(o))
    for o, val in enumerate(uniq):
       
        sumoffactor *= (val**(counteach[o]+1)-1)/(val-1)
    sumoffactor-=i
    
    
    a = primefactor(sumoffactor)
    uniq = unique(a)
    counteach = []
    sumoffactor2 = 1
    for o in uniq:
        counteach.append(a.count(o))
    for o, val in enumerate(uniq):
       
        sumoffactor2 *= (val**(counteach[o]+1)-1)/(val-1)
    sumoffactor2-=sumoffactor
       
    if sumoffactor2 == i and sumoffactor2 != sumoffactor:
        validnumbers.append(i)
        print(i)
print(validnumbers)
summ = 0

for i in validnumbers:
    summ+=i

summ-=1
print(summ)

    


