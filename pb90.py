import itertools


a = [0,1]
b =[0,4]
c= [0,9,6]
d = [1,6]
e = [2,5]
f = [3,6,9]
g = [4,9,6]
h = [6,4,9]
j = [8,1] # 1,2,4,6,7,8
pss = [[0,1],[0,4],[0,[9,6]],[1,[9,6]],[2,5],[3,[9,6]],[4,[9,6]],[8,1]]

def isvalid(arr):
    check = [[0,1],[0,4],[0,[9,6]],[1,[9,6]],[2,5],[3,[9,6]],[4,[9,6]],[8,1]]
    for j in check:

        if type(j[0]) != list and type(j[1]) != list:
            if (j[0] in arr[0] and j[1] in arr[1]) or (j[0] in arr[1] and j[1] in arr[0]):
                print("yee")
                print(j)
                continue
                
            else:
                print("ff")
                print(j)
                return False
        elif type(j[0]) != list and type(j[1])== list:
            if (((j[1][1] in arr[0]) or (j[1][0] in arr[0])) and j[0] in arr[1]) or (((j[1][1] in arr[1]) or ( j[1][0] in arr[1]))  and (j[0] in arr[0])):
                print("yee")
                print(j)
                continue
            else:
                print("ff")
                print([[0, 1, 2, 3, 4, 9], [1, 4, 5, 7, 8, 9]])
                print(j)
                return False
    return True


allnums =  [0,1,2,3,4,5,6,7,8,9]
allints = [0,1,2,3,4,5,6,8,9]

def generate_combinations(array, n):
    return [list(comb) for comb in itertools.combinations(array, n)]

def collapse(arr):
    a = []
    for i in arr:
        if i not in a:
            a.append(i)
    if 9 in a and 6 in a:
        
        b = list.copy(a)
        b.remove(9)
        c = list.copy(a)
        c.remove(6)
        
        return [b,c]
        
    return a
    

def findconj(arr, nums):
   
    copy = list.copy(nums)
    
    conj1 = list.copy(nums)
    if 9 in arr or 6 in arr:
        if 9 in arr:
            copy.remove(9)
        if 6 in arr:
            copy.remove(6)
        for i in arr:
            if i != 9 and i != 6:
                copy.remove(i)
        return copy
    if 9 not in arr and 6 not in arr:
       for i in arr:
           conj1.remove(i)
           
       
       conj2 = list.copy(conj1)
       conj1.remove(6)
       conj2.remove(9)
    return [conj1, conj2]



ap = []

def zone(t,arr, m):
   
    global ap
    mag = 2
    for i in m:
        if t == i:
            mag = 3
    
    if t == -1:
        ap.append(arr[::-1])
        return 0
    for i in range(mag):
        c = list.copy(arr)
        c.append(i)
        zone(t-1,c,m)
    




def allconjfopt(arr):
    if len(arr) > 6:
        return [1,1,1,1,1,1,1,1]
    print(arr)
    global ap
    tp = -1
    certain = []
    vary = []
    all = []
    for i in arr:
        if type(i) == list:
            tp+=1
            vary.append(i)
        else:
            certain.append(i)
    m = []

    for count,i in enumerate(vary):
        
        if len(i) == 3:
             m.append(count)
    
    zone(tp,[],m)


    for i in ap: 
        ins = list.copy(certain)
        for count,j in enumerate(i):
            if vary[count][j] not in ins:
                ins.append(vary[count][j])
        all.append(ins)
    ap = []
    all2 = []

    for i in all:
        if i not in all2:
            all2.append(i)
    
    return all2


def pattern_in_lists(array, pattern):
    def matches(sublist, pattern):
        if not isinstance(sublist, list) or not isinstance(pattern, list):
            return False
        if len(sublist) < len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] is not None and pattern[i] != sublist[i]:
                return False
        return True

    for sublist in array:
        if matches(sublist, pattern):
            return True
    return False


def findconj2(arr):

    add = []

    ps = [[0,1],[0,4],[0,[9,6]],[1,[9,6]],[2,5],[3,[9,6]],[4,[9,6]],[[9,6],4],[8,1]]
    for i in ps:
        print(i)
        if type(i[1]) != list and type(i[0]) != list:
            if i[0] in arr and i[1] not in arr:
                if i[1] not in add:
                    add.append(i[1])
                    print("a1")
                  
            elif i[0] not in arr and i[1]  in arr:
                if i[0] not in add:
                    add.append(i[0])
                    print("a2")
             
            elif i[0] in arr and i[1]  in arr:
                if i[0] not in add and i[1] not in add and [i[0], i[1]] not in add and pattern_in_lists(add, [i[0], None,None]) == False and pattern_in_lists(add, [i[1], None,None]) == False:
                    add.append([i[0], i[1]])
                    print("a3")
        
        elif type(i[0]) != list and type(i[1]) == list:
            if i[0] in arr and (i[1][0] not in arr and i[1][1] not in arr):
                if i[1] not in add and pattern_in_lists(add, [None, 9,6]) == False:
                    add.append(i[1])
                    print("a4")
                
      
            elif i[0] not in arr and (i[1][0]  in arr or i[1][1] in arr):
                if i[0] not in add:
                    add.append(i[0])
                    print("a5")

            elif i[0] in arr and (i[1][0]  in arr or i[1][1] in arr):
                if i[0] not in add and i[1] not in add and pattern_in_lists(add, [None, 9,6]) == False:
                    add.append([i[0],i[1][0],i[1][1]])
                    print("a6")
        elif type(i[0]) == list and type(i[1]) != list:
            if i[1] in arr and (i[0][0] not in arr and i[0][1] not in arr):
                if i[0] not in add and pattern_in_lists(add, [None, 6,9]) == False:
                    add.append(i[0])
                    print("a7")
      
            elif i[1] not in arr and (i[0][0]  in arr or i[0][1] in arr):
                if i[1] not in add:
                    add.append(i[1])
                    print("a8")

            elif i[1] in arr and (i[0][0]  in arr or i[0][1] in arr):
          
                if i[0] not in add and i[1] not in add and pattern_in_lists(add, [None, 9,6]) == False:
                    add.append([i[1],i[0][0],i[0][1]])
                    print("a9")
   

    print("add")
    print(add)
    return allconjfopt(add)
        




    
r = 0
    
alldices = []
allcombs= []
allcombswr = []
for a1 in a:
    for b1 in b:
        for c1 in c:
            for d1 in d:
                for e1 in e:
                    for f1 in f:
                        for g1 in g:
                            for h1 in h:
                                for j1 in j:
                                    r+=1 
                                    col = collapse([a1,b1,c1,d1,e1,f1,g1,h1,j1])
                                    if type(col[0]) != list:
                                        conjs = findconj2(col)
                                        for m in conjs:
                                            oo = [col, m]
    
                                            if len(oo[1]) < 7 and len(oo[0]) < 7:
                                                
                                                alldices.append(oo)
                                    else:
                                        for al in col:
                                            conjs = findconj2(al)
                                            for m in conjs:
                                                oo = [al, m]
        
                                                if len(oo[1]) < 7 and len(oo[0]) < 7:
                                                    
                                                    alldices.append(oo)
    

print(r)

def subtract_arrays(arr1, arr2):
    return [item for item in arr1 if item not in arr2]


def allcombsfrom(arr):
    sub = subtract_arrays( [0,1,2,3,4,5,6,7,8,9], arr)

    lensub = 6-len(arr)
    combs = generate_combinations(sub, lensub)

    all = []
    for i in combs:
        c = list.copy(arr)
        c.extend(i)
       
        list.sort(c)
        all.append(c)
 
    return all

ndices = []

nndices = []


for i in alldices:
    if i not in ndices:
        ndices.append(i)
#
#for i in ndices:
#    for c, count in enumerate(i):
#        ii = 0
#        if count == 0:
#            ii = 1
#        if 9 in c and 6 not in c:
#            ind = i.index(9)
#            n = list.copy(c)
#            n[ind] = 6
#            if n not in nndices:
#                nndices.append(n)
#            if c not in nndices:
#                nndices.append(c)
#    
#        if 6 in c and 9 not in c:
#            ind = i.index(6)
#            n = list.copy(c)
#            n[ind] = 9
#            if n not in nndices:
#                nndices.append(n)
#            if  not in nndices:
#                nndices.append(i)
#    
#        if 6 in i[0] and 9 in i[0]:
#            ind = i.index(6)
#            n = list.copy(i)
#            n[i] = 9
#            if n not in nndices:
#                nndices.append(n)
#            if i not in nndices:
#                nndices.append(i)
#    
#        if 9 in i[0] and 6 in i[0]:
#            ind = i.index(9)
#            n = list.copy(i)
#            n[i] = 6
#            if n not in nndices:
#                nndices.append(n)
#            if i not in nndices:
#                nndices.append(i)
#        
#        

combinations = generate_combinations([0,1,2,3,4,5,6,7,8,9], 6)
combc = list.copy(combinations)
for i in combinations:
    

    for j in pss:
        if type(j[0]) != list and type(j[1]) != list:
            if j[0]  in i or j[1]  in i:
                continue
            else:
                if i == [1,2,4,6,7,8]:
                    print(j)
                    print("jey")
                    print("a1")
                combc.remove(i)
                break
                

        elif type(j[0]) == list and type(j[1]) != list:
            if j[0][1] in i or j[0][0]  in i or j[1]  in i:
                continue
            else:
                if i == [1,2,4,6,7,8]:
                    print("jey")
                    print("a2")
                combc.remove(i)
                break

        elif type(j[0]) != list and type(j[1]) == list:
            if j[1][1] in i or j[1][0] in i or j[0]  in i:
                continue
            else:
                if i == [1,2,4,6,7,8]:
                    print("jey")
                    print("a3")
                combc.remove(i)
                break

print(len(combinations))





co = 0
cs = []
for count, j in enumerate(combinations):
    print(count)
    for c in combinations:
        print(c)
        if isvalid([j,c]):
            cs.append([j,c])
            co+=1

print(combc)
print(co)

ff = []

reverse = 0 
for i in cs:
    print(i)
    if  [i[1],i[0]] in cs:
        reverse += 1
        
def find_reversed_pairs(array_pairs):
    for i in range(len(array_pairs)):
        for j in range(i + 1, len(array_pairs)):
            set_a = set(map(tuple, array_pairs[i]))
            set_b = set(map(tuple, array_pairs[j]))
            for a in set_a:
                if (a[::-1] in set_b):
                    return (i, j, a, a[::-1])
    return None

result = find_reversed_pairs(cs)

if result:
    i, j, a, b = result
    print(f"Reversed pair found between arrays at indices {i} and {j}: {a} <=> {b}")
else:
    print("No reversed pair found in the array list.")


print(len(cs))

d = 0
for c,i in enumerate(cs):
    if i in cs[c:]:
        d +=1

print(d)
print(len(cs))

