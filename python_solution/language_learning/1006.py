v = input().split()
a = float(v[0])
b = float(v[1])

l = 2*(a+b)
s = a*b
if (a > 0) & (b > 0):
    print("%.2f" % l)
    print("%.2f" % s)
else:
    print ("Input Error")
    