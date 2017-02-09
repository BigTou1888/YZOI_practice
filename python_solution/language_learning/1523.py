n=int(input())

i=1
sum=0
while i<=n:
    mul=1
    j=i
    while j>=1:
        mul*=j
        j-=1
    sum+=mul
    i+=1
print(sum)