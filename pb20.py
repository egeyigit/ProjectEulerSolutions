from re import A


def factorial(a):
    if a == 1:
        return a
    else:
        return a*factorial(a-1)

st100 = str(factorial(100))
sum = 0
for i in st100:
    sum+=int(i)
print(sum)