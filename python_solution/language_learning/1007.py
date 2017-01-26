v = input().split()
a = float(v[0])
b = float(v[1])

if (a==0) & (b==0):
    print ("0.0000")
elif a==0:
    print ("Input Error")
else:
    sol = (0-b)/a
    print ("%.4f" % sol)