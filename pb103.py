import itertools
from itertools import product

nap = [11,18,19,20,22,25]
new = [19, 30, 37, 38, 39, 41, 44]

def generate_sorted_arrays():
    # Generate all possible arrays with elements ranging from -2 to 2
    all_arrays = list(product(range(-2, 3), repeat= 6))
    
    # Sort the arrays by their sum
    sorted_arrays = sorted(all_arrays, key=sum)
    
    return sorted_arrays



def subtract_arrays(arr1, arr2):
    return [item for item in arr1 if item not in arr2]


def generate_combinations(array, n):
    return [list(comb) for comb in itertools.combinations(array, n)]


arrays = generate_sorted_arrays()


def isspe(arr):
    l = len(arr)
    lf = 0
    allsums = []
    for i in range(1,l):
  
        lf = i
        combs = generate_combinations(arr, i)
   
        for c in combs:
            s = sum(c)
            a = subtract_arrays(arr,c)
            for j in range(1,len(c)+1):
                combs2 = generate_combinations(a, j)
               
                for j2 in combs2:
                    s2 = sum(j2)
                    if ([s2,s]) not in allsums and len(c) != len(j2):
                        allsums.append([s2,s])
    for i in allsums:
        if i[0] == i[1]:
            return False
    return True

#for i in range(10000):
#    print(isspe([19, 30, 37, 38, 39, 41, 44]))
#

        
#tarr = []
#def dsum(arr,c):
#    global tarr
#    sums = c
#    print(arr)
#    if arr == []:
#        tarr.append(sums)
#    for count, i in enumerate(arr):
#       
#        
#        b = list.copy(sums)
#        b.append(i)
#        dsum(arr[count+1:],b)
#    
#dsum([19, 30, 37, 38, 39, 41, 44],[])
#print(tarr)
#for i in tarr:
#    if len(i) == 2:
#        print(i)
#



for arr in arrays:
    combined_array = [arr[i] + new[i] for i in range(6)]
    if 
