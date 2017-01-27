import math

v = input().split()
v1 = int(v[0])
v2 = int(v[1])

vmin = v1
if v2<v1:
    vmin = v2

n = vmin
while n >= 2:
    if (v1 %n == 0) & (v2 % n == 0):
        break
    else:
        n = n-1

o1 = n
o2 = v1 * v2 / n
print(o1)
print(int(o2))
