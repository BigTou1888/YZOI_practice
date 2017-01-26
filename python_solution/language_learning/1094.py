import math

v = input().split()
a = float(v[0])
b = float(v[1])
c = float(v[2])
    
if a == 0:
    if b == 0:
        if c == 0:
            print("Many Roots")
        else:
            print("No Roots")
    else:
        x = 0-c/b
        print ("%.2f" % x)
else:
    s = b*b - 4 *a *c
    if s == 0:
        x = 0-b/2/a
        print ("%.2f" % x)
    elif s < 0:
        print ("No Roots")
    else:
        x1 = (0 - b - math.sqrt(s))/2/a
        x2 = (0 - b + math.sqrt(s))/2/a
        if x1 < x2:
            print("%.2f %.2f" % (x1, x2))
        else:
            print("%.2f %.2f" % (x2, x1))