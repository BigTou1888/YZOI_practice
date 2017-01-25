
i = 0
while 1:
    value = input().split()
    a = 0
    l = 0
    if (int(value[0]) == 0) | (int(value[1]) == 0) : 
        a = 0
        l = 0
    else :
        a = int(value[0])/ int(value[1])
        l = a * 4 * int(value[1]) * int(value[1]) /2
    print (int(l))
    i = i+1