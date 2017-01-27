t = int( input())

i = 0
status = []
while i < t:
    s = int(input())
    n = 0
    p = 1
    while p<(s/2):
        if s%p == 0:
            n = n+p
        p = p+1
    if n==p:
        status.append("Perfect Number")
    elif n<p:
        status.append("Insufficient Number")
    else:
        status.append("Excess Number")

    i = i+1
            
i = 0
while i < t:
    print(status[i])
    i=i+1
