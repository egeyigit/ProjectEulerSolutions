primes = [2,3,5,7,11,13,17,19]
primes2 = primes[::-1]
def primefactor(a):
    factorset = []
    index = 7
    b = a
    while b > 1:

        if b%primes[index]== 0:
            factorset.append(primes[index])
            b = b/primes[index]
        index-=1
        if index==-1:
            index = 7

    return(factorset)


lists = [[] for _ in range(8)]

for i in range(2,21):
    
    factored = primefactor(i)
    print(factored)
    for index, value in enumerate(primes):
        print(value)
        countedprime = factored.count(value)
        lists[index].append(countedprime)

finalfactors=[]
for i in lists:
    finalfactors.append(max(i))
sum=1
print(finalfactors)
for i, value in enumerate(finalfactors):
    sum*= (primes[i] ** value)
print(sum)