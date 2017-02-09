import math
n = int(input())
upper = int(math.sqrt(n))
i = 2
prime =True
if n ==1:
    prime = False
while i <= upper:
    if n%i==0: 
        prime=False
    i+=1
if prime :
    print("Yes")
else:
    print("No")
