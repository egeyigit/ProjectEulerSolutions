

primes = [2]
import math

for i in range(3,2*10**6,2):
    if (i-1)%10000==0:
        print(i)
    isprime= True
    for each in primes:
        if i%each==0:
            isprime = False
        if each > math.sqrt(i):
            break
    
    if isprime == True:
        primes.append(i)


        




def primefactor(a):
    factorset = []
    index = 100000
    b = a
    while b > 1:
        
        if b%primes[index]== 0:
            factorset.append(primes[index])
            b = b/primes[index]
        index-=1
        if index==-1:
            index = 100000

    return(factorset)


def unique(a):
    toreturn = []
    for i in a:
        if i not in toreturn:
            toreturn.append(i)
    return(toreturn)


for i in range(100000):
    
    factorcount = 1
    trnum = i*(i+1)/2
    print(trnum)
    primefactors = primefactor(trnum)
    
    uniquef = unique(primefactors)
    print(uniquef)
    for c in uniquef:

        factorcount *= (primefactors.count(c)+1)
    print(factorcount)
    if factorcount > 500:
        print(trnum)
        break