v = input().split()
a = int(v[0])
b = int(v[1])
c = int(v[2])

if a > b:
    if a > c:
        print (a)
    else:
        print (c)
else:
    if b > c:
        print (b)
    else:
        print (c)
        