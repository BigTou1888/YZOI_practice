mxn=input().split()
m1=int(mxn[0])
n1=int(mxn[1])
i=0
mattrix_1=[]
while i < m1:
    row=[]
    for x in input().split():
        row.append(int(x))
    mattrix_1.append(row)
    i+=1
blank=input()

mxn=input().split()
m2=int(mxn[0])
n2=int(mxn[1])
i=0
mattrix_2=[]
while i < m2:
    row=[]
    for x in input().split():
        row.append(int(x))
    mattrix_2.append(row)
    i+=1
    
i=0
while i < m1:
    j=0
    while j<n2:
        result = 0
        k=0
        while k<n1:
            result+=mattrix_1[i][k]*mattrix_2[k][j]
            k+=1
        print(result, end='')
        if j < n2-1:
            print(' ', end='')
        else:
            print('')
        j+=1
    i+=1