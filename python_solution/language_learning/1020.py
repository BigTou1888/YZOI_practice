
c = int(input())
v = input().split()


i = 0
p = 0
n = 0
z = 0
while i < c:
    if float(v[i]) > 0 :
        p = p+1
    elif float(v[i]) <0:
        n = n+1
    else:
        z = z+1
    i = i+1

        

print(n, z, p)

