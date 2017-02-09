
n = int(input())
num = input().split()

i=0
data=[]
rank=[]
while i < n:
    value = int(num[i])
    pos = 0
    while pos<i:
        if value < data[pos]:
            data.insert(pos, value)
            rank.insert(pos, (i+1))
            break
        pos+=1
    if pos == i:
        data.append(value)
        rank.append(i+1)
    i+=1
i=0
while i < n:
    print("%d %d" % (data[i], rank[i]))
    i+=1


