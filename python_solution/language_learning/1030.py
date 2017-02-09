
n = int(input())
num = input().split()
maxim = 0
minium = 10
sum = 0
i=0
while i < n:
    score = float(num[i])
    if maxim < score:
        maxim = score
    if minium > score:
        minium = score
    sum+=score
    i+=1
avg = (sum - maxim-minium)/(n-2)
print("%.2f" % avg)


