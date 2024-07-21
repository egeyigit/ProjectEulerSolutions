
import os
import math
# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the pb98.txt file
file_path = os.path.join(script_dir, "hey.txt")

all =[]

with open(file_path , "r") as f:
    ws = f.read()
    # Strip any potential surrounding quotes and newlines
    ws = ws.strip()
    # Handle the case if the file starts and ends with quotes
    if ws.startswith('"') and ws.endswith('"'):
        ws = ws[1:-1]
    # Split the string by ","
    warr = ws.split('","')


dicws = {}

sameps = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[]}

pairs = []


def add_to_dict(key, value):
    # Use setdefault to create a list if the key doesn't exist
    dicws.setdefault(key, []).append(value)

for i in warr:
    add_to_dict(len(i), i)




def add_and_sort_letters(word):
    # Sort the letters of the word and return the sorted list
    return sorted([char for char in word])


def sort_digits(number):
    # Convert the number to a string to iterate over each digit
    num_str = str(number)
    
    # Initialize an empty array to store the digits
    digits = []
    
    # Iterate over each character in the string
    for char in num_str:
        # Convert the character to an integer and append to the array
        digits.append(int(char))
    
    # Sort the array in increasing order
    digits.sort()
    
    # Return the sorted array
    return digits

ps = []


for key, val in dicws.items():

    if key < 14:
        for i in val:

            a = add_and_sort_letters(i)
            if a not in sameps[key]:
                sameps[key].append(a)
            else:
                
                pairs.append([dicws[key][sameps[key].index(a)],i])
                sameps[key].append(a)

    
moret4 = []

for i in pairs:
    
    moret4.append(i)

print(moret4)



s4 = []
s5 = []
s6 = []
s7 = []




# 31622
for i in range(50000):
    
    a= sort_digits(i**2)
    if(a in all):
        o = all[all.index(a)+1]
        ps.append([o, i**2])


    all.append(a)
    all.append(i**2)




for i in ps:
    a = str(i[0])
    
    if len(a) == 4:
        print("appended")
        s4.append(i)
    if len(a) == 5:
        s5.append(i)
    if len(a) == 6:
        s6.append(i)
    if len(a) == 7:
        s7.append(i)






def ismatch(p1, p2):
    match1 = []
    match2 = []
    p11 = [str(p1[0]), str(p1[1])]
    for i,c in enumerate(p11[0]):
        a = p11[1].index(c)
        match1.append([i,a])
        match2.append([a,i])

    nmatch = []
    p22 = [str(p2[0]), str(p2[1])]
    
    for i,c in enumerate(p22[0]):
        a = p22[1].index(c)
        nmatch.append([i,a])

    if nmatch == match1 or nmatch == match2:
        return True

    return False



for i in moret4:

    if len (i[0]) == 4:
        for j in s4:
            if ismatch(i,j):
                print(i,j)
    if len (i[0]) == 5:
       for j in s5:
       
           if ismatch(i,j):
               print(i,j)
    if len (i[0]) == 6:
       for j in s6:
          
           if ismatch(i,j):
               print(i,j)
    if len (i[0]) == 7:
       for j in s7:
           if ismatch(i,j):
               print(i,j)
    

print(ismatch([1234,4231],["abcd","dcba"]))
