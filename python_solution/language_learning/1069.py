import math
def heron_formular (a, b, c):
    s = (a+b+c)/2
    A = math.sqrt(s * (s-a) * (s-b) * (s-c))
    return A


l = []

input_param  = input().split()

for x in input_param:
    l.append(float(x))

sum = 0
sum = sum+heron_formular (l[0], l[5], l[6])
sum = sum+heron_formular(l[6], l[7], l[1])
sum = sum+ heron_formular(l[7], l[8], l[4])
sum = sum+heron_formular(l[8], l[2], l[3])
print("%.2f" % sum)
