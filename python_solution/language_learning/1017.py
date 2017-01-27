
d = int(input())
n0 = 1
n1 = 1
n2 = 0
n3 = 0


i = 1

while i < d:
    n3 = n2+n3
    n2 = n1
    n1 = n3
    i = i+1

print(n3+n2+n1)

