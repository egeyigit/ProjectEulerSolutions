import math


counts = []
def findminx(d):
    global counts
    x = 1 
    y = 1
    count = 1
    b = False
    while ( x*x - d*y*y != 1 ):
        x = d* count -1
      
        sqrt_val = math.isqrt(int((x - 1) * (x + 1) / d))
        if sqrt_val * sqrt_val == (x - 1) * (x + 1) / d and sqrt_val != 0:

            y = math.sqrt((x-1)*(x+1)/d)
        else: 
            x = d* count + 1
      
            sqrt_val = math.isqrt(int((x - 1) * (x + 1) / d))
            if sqrt_val * sqrt_val == (x - 1) * (x + 1) / d and  math.sqrt((x-1)*(x+1)/d) != 0:

                y = math.sqrt((x-1)*(x+1)/d)
        count += 1

        if count > 6000000: 
            b = True
            break
    print(count)
    if count != 6000001:
        counts.append([count/d, d])
    print(x,y)
    



    if b:
        return -1
    return x



def findall(d, m):
    cts = []
    x = 1 
    y = 1
    count = 1
    b = False
    for i in range(m):
        
        x = d* i -1
        
        sqrt_val = math.isqrt(int((x - 1) * (x + 1) / d))
        if sqrt_val * sqrt_val == (x - 1) * (x + 1) / d and sqrt_val != 0:

            y = math.sqrt((x-1)*(x+1)/d)
        else: 
            x = d* i + 1
        
            sqrt_val = math.isqrt(int((x - 1) * (x + 1) / d))
            if sqrt_val * sqrt_val == (x - 1) * (x + 1) / d and  math.sqrt((x-1)*(x+1)/d) != 0:

                y = math.sqrt((x-1)*(x+1)/d)

        if (x*x - d*y*y == 1):
            cts.append(i)

    return cts

    
print(findall(19,1000))

    

#arr = []
#for i in range(2,150):
#    a = findminx(i)
#    print(a)
#    arr.append(a)
#print(max(arr))
#print(arr.index(max(arr)))
#print(arr)
#
#for c,d in enumerate(arr):
#    if d != -1:
#        print(c+2)
#
#print(counts)