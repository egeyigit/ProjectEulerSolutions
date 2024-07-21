
from unicodedata import name


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"




with open("names.txt","r") as file:
    a = str(file.read())
    namessplitted = a.split('","')
    
print(len(namessplitted))
print(alphabet.index("O"))
for s in range(5161):
    print(s)
    for i, val in enumerate(namessplitted):
        
        if i == 5162:
            break
        sort1 = 0
        sort2 = 0
        index = 0
        
        while sort1 == sort2:
            try:

                sort1+= int(alphabet.index(val[index]))
            except:
                pass
            try:
                sort2+= int(alphabet.index(str(namessplitted[i+1][index])))
            except:
                pass
            index+= 1
    
    
        if sort1 > sort2:
            namessplitted[i] = namessplitted[i+1]
     
            namessplitted[i+1] = val
        print(namessplitted)
        
        
