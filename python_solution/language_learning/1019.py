import math
while 1 :
    v = input().split()
    a = float(v[0])
    b = float(v[1])
    c = float(v[2])
    
    if (a+b-c>0) & (b+c-a>0) & (a+c-b>0):
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print ("%.2f" % area)
    else:
        print (0)
