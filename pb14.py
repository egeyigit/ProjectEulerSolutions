def collabz(number):

    sum = 1
    value = collabt2(number)
    while value != 1:
        sum += 1
        value = collabt2(value)
    
    return sum

def collabt2(number):
    if number%2==0:
        return number//2
    else:
        return int(3 * number + 1)

maxval = 1
max = 1

for i in range(1,1000001):
    value = collabz(i)
    if maxval < value:
        maxval = value
        max = i

print(max)

