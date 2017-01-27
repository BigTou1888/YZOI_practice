c = int( input())

i = 0

total = 0
while i < c:
    li = []
    li = input().split()
    p = int(li[0])
    d = int(li[1])
    if d != 10:
        total = d*p/10 +total
    i = i+1
            
        
print("%.2f" % total)

