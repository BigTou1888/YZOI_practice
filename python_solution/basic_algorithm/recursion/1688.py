def combination(n):
    com=[1,2]
    i=2
    while i<n:
        com_tmp = com[i-1]+com[i-2]
        com.append(com_tmp)
        i+=1
    if n==0:
        return 1
    else:
        return com[n-1]
n=int(input())
i=0
while i<n:
    m=int(input())
    result = combination(m-1)
    print(result)
    i+=1
