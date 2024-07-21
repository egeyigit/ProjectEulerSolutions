primes = [2]
import math
sum = 0
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

for i in primes:
    sum+= i
        
print(sum)