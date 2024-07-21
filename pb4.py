from termios import FF1


f1 = 999
f2 = 999

def checkpal():
    global f1,f2
    check = str(f1*f2)
    if check == check[::-1]:
        print()
        
        return (f1*f2)
    else: 
        return (False)

palinds = []
checking = True
for i in range(1000):
    f1= 999-i
    for f in range(1000):
        f2= 999-f
        if checkpal() != False:
            palinds.append(checkpal())

print(max(palinds))
    
    
        