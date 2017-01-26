import math

v = input().split()
p = float(v[0])
w = float(v[1])
l = float(v[2])
 
r = 1
offset = 0.02
if l <= 300:
    offset = 0
    
if w <2:
    r = 0.98
elif (w< 5) & (w >=2):
    r = 0.95
elif (w>=5):
    r = 0.92
r = r + offset

total = p * l * r


print (round(total))
