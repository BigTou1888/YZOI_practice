import math
num = input()
num = int(num)
i = 0
coor = []
while i < num :
    coor.append(input().split())
    i = i+1

radium = []

radium.append(0)
i = 0
while i < num:
    x = float(coor[i][0])
    y = float(coor[i][1])
    l = math.sqrt (x*x+y*y)
    done = 0
    year = 0
    while year < len(radium):
        if l < radium[year]: 

            done = 1
            break
        else: year = year+1

    if done: 
        print("Property %d: This property will begin eroding in year %d." % (i+1, year))
    else: 
        year = year -1
        while l >= radium[year]:
            r = math.sqrt((100 + radium[year]*radium[year]*3.14)/3.14) 
            radium.append(r)
            year = year +1
        print("Property %d: This property will begin eroding in year %d." % (i+1, year))
    i = i+1
print("END OF OUTPUT.")