def fact(number):
    if number==1:
        return 1
    if number > 1:
        return fact(number-1) * number
print(fact(5))
print(fact(40)/fact(20)/fact(20))