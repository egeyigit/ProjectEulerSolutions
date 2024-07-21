

def ne(n):
    if n == 0:
        return 2
    if int(n/3)*3+2 == n:
        return (int(n/3)+1)*2
    else:
        return 1

print(ne(11))

def nplus(n, fraction):

    if n < 0:
        return fraction[0]

    c = ne(n)
    if type(fraction) == int:
        fraction1 = [1, fraction]
    else:
        fraction1 = [fraction[1], fraction[0]]
    

    return nplus(n-1,[c*fraction1[1] + fraction1[0], fraction1[1]])


st = str(nplus(98, ne(99)))
t = 0

for i in st:
    t += int(i)
print(t)