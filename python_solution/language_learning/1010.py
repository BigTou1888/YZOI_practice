v = input().split()
x1 = float(v[0])
y1 = float(v[1])
x2 = float(v[2])
y2 = float(v[3])
x3 = float(v[4])
y3 = float(v[5])

xmin = x1
xmax = x2

ymin = y1
ymax = y2

if x2 < x1:
    xmin = x2
    xmax = x1
if y2 < y1:
    ymin = y2
    ymax = y1

if (x3 < xmin) | (x3 > xmax) | (y3 < ymin) | (y3 > ymax):
    print ("False")
else:
    print("True")