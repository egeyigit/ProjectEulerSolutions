a = 600851475143%131195
print(a)

def calculateprime(b):
    foundprime = False
    variable = b
    counter = 0

    factors = []
    for i in range(b):
        if b%(i+1) == 0:
            factors.append(i+1)
    print(factors)

calculateprime(a)
    
      