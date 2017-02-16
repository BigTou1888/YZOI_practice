global x1, x2, y1, y2
def path_find (m,n):
    global x1, x2, y1, y2

    if (m == 1) & (n==1):
        return 1
    else:
        down=0
        left=0
        if (((n-1)<=y2) & ((n-1)>=y1) & (m<=x2) & (m>=x1)) | (n==1):
            down=0
        else:
            down = path_find(m, (n-1))
        
        if (((m-1)<=x2) & ((m-1)>=x1) & (n<=y2) & (n>=y1)) | (m==1):
            left=0
        else:
            left = path_find((m-1), n)
    
        return down+left


    
c=input().split()
m=int(c[0])
n=int(c[1])

c=input().split()

x1=int(c[0])
y1=int(c[1])
x2=int(c[2])
y2=int(c[3])

if x1 >x2:
    tmp = x1
    x1=x2
    x2=tmp
if y1>y2:
    tmp = y1
    y1=y2
    y2=tmp

result = path_find (m,n)

print(result)