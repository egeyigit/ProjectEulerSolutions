primes = [2]
import math


for i in range(3,2*10**6,2):
    
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

print(unique(primefactor(35)))
i = 0
while True:
    i+=1
    
    if len(unique(primefactor(i))) == len(unique(primefactor(i+1))) == len(unique(primefactor(i+2)))  == len(unique(primefactor(i+3))) == 4:
        print(i)
        break