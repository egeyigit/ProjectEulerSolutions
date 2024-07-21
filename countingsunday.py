


months = [31,28,31,30,31,30,31,31,30,31,30,31]




date = [1,1901]

numberofmonday = 0





days = 2

while date != [31,2000]:
    currentmonth = 0
    for i in months:
        s = i
        if i == 28 and date[1]%4==0:
            s = i+1
        for c in range(1,s+1):

            date[0]+= 1
            days += 1
            print(date)
            if date[0] == 1 and days%7== 0:
                numberofmonday +=1
            if date == [31,2000]:
                break
        if date == [31,2000]:
                break
        date[0] = 0
    if date == [31,2000]:
                break

    date[1] += 1

print(numberofmonday)