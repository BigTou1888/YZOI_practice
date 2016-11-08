from math import *
in_value=[]
for x in input().split():
    in_value.append(int(x))
a = in_value[0]
b = in_value[1]
alpha = radians(in_value[2])
out_value = sqrt(a*a + b*b + 2*a*b*cos(alpha))
print("%.4f" % out_value)
