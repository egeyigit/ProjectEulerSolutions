import math
primelist=[]
num = 1
lognum = 0
while lognum < 10000 or lognum > 10002:  
    num += 1 
    lognum = num/math.log(num,2)




for i in range(num):
    primelist.append(i)

print(122)
a = int(math.sqrt(num))

for i in range(2,a+1):
    
    if i == 20:
        print(primelist[20])
    for c in range(int(num/i)):
    
        try:
    
            primelist.remove(c*i)
    
        except:
    
            pass

            
print(primelist[10])




