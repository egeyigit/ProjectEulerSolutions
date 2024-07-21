def gcd(a, b):
 
    if (a == 0):
        return b
    return gcd(b % a, a)
 
def lcm(a,b):
    return(a*b/gcd(a,b))

print(lcm(15,12))

# A simple method to evaluate
# Euler Totient Function
def phi(n):
 
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result+=1
    return result

val = []


#for i in range(1000000):
#    if i % 10000 == 0:
#        print(i)
#    val.append(i/phi(i))
#
#print(val.index(val(max)))
#
def factorial(a):
    if a == 1:
        return a
    else:
        return(factorial(a-1)*a)
n = 2 
while factorial(n) < 1000000:
    n+=1

print(2*factorial(n-1))

