n = int(input())
i=0
sum = 0
num = input().split()
while i < n:
    sum += float(num[i])
    i+=1
    
avg = sum/n

print("%.2f %.2f" % (sum,avg))