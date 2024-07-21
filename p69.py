#n < 1 million we need to find number with most distinct prime number factor

primes = [2,3,5,7,11,13,17,19,23]


divisor = 1
cur = 1
for i in primes:
    if cur * i < 1000000:
        cur *= i
        divisor * (1-1/i)
    else:
        break
print(cur)


