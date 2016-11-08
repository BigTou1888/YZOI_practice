in_value=[]
cnt = 0
sum = 0
for x in input().split():
    in_value.append(int(x))
    cnt = cnt+1
    sum = sum + int(x)

out_value = sum/cnt
print("%.3f" % out_value)
