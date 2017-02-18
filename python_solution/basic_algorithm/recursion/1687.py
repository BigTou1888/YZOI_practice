def combination(n):
    com=[1,2]
    i=2
    while i<n:
        com_tmp = com[i-1]+com[i-2]
        com.append(com_tmp)
        i+=1
    return com[n-1]
n=int(input())
start=0
end=n
result = combination(n)
print(result)
