

vals = [0,0,0,0,0,0,0,0,0,0]


def fix(p):
    copy = list.copy(p)
    number_counts = {}
    cs = [0,0,0,0,0,0,0,0,0,0]
    consts = []
    for i in p:
        a = 0
        for c in i:
            a+=c
            cs[c-1] += 1
        key = str(a)
        if key in number_counts:
            number_counts[key] += 1
        else:
            number_counts[key] = 1
        consts.append(a)
    print("here")
    print(consts)
    print(number_counts)
    min_key = int(min(number_counts, key=number_counts.get))
    max_key = int(max(number_counts, key=number_counts.get))
    indmin = consts.index(min_key)
    indmac = consts.index(max_key)
    rep = cs.index(3)+1
    addt = max_key - min_key



    ind2 = p[indmin].index(rep)

    copy[indmin][ind2] = copy[indmin][ind2]+addt
    return copy




    

def generatepenta(vals):
    penta = [[vals[9],vals[0],vals[1]],[vals[5],vals[1],vals[0]],[vals[6],vals[2],vals[3]],[vals[7],vals[3],vals[4]],[vals[8],vals[4],vals[0]]]
    pst =""
    vals= []

    penta = fix(penta)
    for c in penta:
        vals.append(c[0])

    ind = vals.index(min(vals))

    for i in range(ind,5):
        for j in penta[i]:
            pst+=str(j)
    for i in range(0,ind):
        for j in penta[i]:
            pst+=str(j)

    
    return int(pst)
allcombs = []

ava = [1,2,3,4,5,6,7,8,9,10]
ava2 = [1,2,3,4,5,6,7,8,9,10]
for a in range(1,11):

  
    ava2 = list.copy(ava)
    ava2.remove(a)

    print(ava2)
    for b in ava2:
        print("b",b)
        if b+a < 19:
            ava2.remove(b)
            vals[8] = a
            vals[0] = b
            for c in ava2:
                
                ava2.remove(c)
                d = b+a - c
    
                if d not in ava2 or d + c >= 19:
                    ava2.append(c)
                    continue
                ava2.remove(d)
                vals[3] = c
                vals[7] = d
    
                for g in ava2:
                   
                    const = (d + c + g) 
                    if const <= 19 and const >= 14:
                        ava2.remove(g)
                        vals[4] = g
    
                        for e in ava2:
                            
                            ava2.remove(e)
                            k = g + d - e
                            ctd = False
                            if k not in ava2 or k + e >= 19:   
                                ava2.append(e)
                                ctd = True
                                continue
                            if (ctd):
                                print("oh no")
                            
                            ava2.remove(k)
                            vals[2] = e
                            vals[6] = k
                            for f in ava2:

                                ava2.remove(f)
                                h = k + c - f

                                if h not in ava2 or h + f >= 19: 
                                    ava2.append(f)
                                    continue
                                ava2.remove(h)
                                vals[1] = f
                                vals[5] = h

                                
                                print("ooo")
                                
                                if h + f + e == const and  f + b + ava2[0] == const:
                                   
                                   vals[9] = ava2[0]
                                   print("yay")
                                   var = [[vals[9],vals[0],vals[1]],[vals[5],vals[1],vals[0]],[vals[6],vals[2],vals[3]],[vals[7],vals[3],vals[4]],[vals[8],vals[4],vals[0]]]
                                   done = True
                                   for vc in var:
                                        if (vc[0] +vc[1] +vc[2]!= const):
                                            done = True
                                   if done:
                                            if len(str(generatepenta(vals))) == 16:
                                               allcombs.append(generatepenta(vals))     
                                   
                                ava2.append(h)
                                ava2.append(f)

                            print(ava2)

                            
                            ava2.append(e)
                            ava2.append(k)

                        ava2.append(g)
                ava2.append(d)
                ava2.append(c)
            ava2.append(b)

    
print(allcombs)
        
print(max(allcombs))