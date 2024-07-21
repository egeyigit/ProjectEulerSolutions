primes = [2]
import math
sum = 0
for i in range(3,1*10**6,2):
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

matchs =[]
for i in range():
    if i**2+1 in primes:
        store = i**2
        first = primes.index(store+1)
        if primes[first+1] == store+3 and primes[first+2] == store+7 and primes[first+3] == store+9 and primes[first+4] == store+13 and primes[first+5] == store+27:
            matchs.append(i)
print(matchs)