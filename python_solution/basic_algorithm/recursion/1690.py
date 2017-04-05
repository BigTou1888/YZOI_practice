def combination(n):
    l=10000000000000000000000000
    com=[]
    for x in range(0,4):
        com.append([])
    
    com[0].append(0)
    com[0].append(1)
    com[0].append(2)
    for x in range(1,4):
        com[x].append(0)
        com[x].append(0)
        com[x].append(0)
    i=3
    while i<=n:
        c=0
        for x in range(0,4):

            com_tmp = com[x][i-1]+com[x][i-2] + c
            c=int(com_tmp/l)
            com_tmp = com_tmp%l
            com[x].append(com_tmp)
        i+=1
    return com
n=int(input())
start=0
end=n
result = combination(n)

for x in range(0,4):
    print("%025d" % result[3-x][n])