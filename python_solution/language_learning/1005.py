v = input().split()
v0 = int(v[0])
v1 = int(v[1])
v2 = int(v[2])

r = [v0, v1, v2]
if v0 > v1:
    if v0 > v2:
        r[2] = v0
        if v1 < v2:
            r[0] = v1
            r[1] = v2
        else:
            r[0] = v2
    else:
        r[1] = v0
        r[0] = v1
else:
    if v1 > v2:
        r[2] = v1
        if v0 < v2:
            r[1] = v2
        else:
            r[0] = v2
            r[1] = v0

print(r[2], r[1], r[0])
    