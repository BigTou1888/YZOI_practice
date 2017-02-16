
def add_on(m, n):
    square = n*(2*m-n+1)/2
    recu = (m+1)*m*n/2
    return(square, recu)
    
def recur_result (m,n): #m>n
    add_on_result = add_on(m, n)
    if n==1:

        return [add_on_result[0], add_on_result[1]]
    else:
        result_prev_recur = recur_result(m, (n-1))
        return [(result_prev_recur[0]+add_on_result[0]), (result_prev_recur[1]+add_on_result[1])]
    
c=input().split()
m=int(c[0])
n=int(c[1])
if m<n:
    tmp=m
    m=n
    n=tmp
result = recur_result(m, n)

print(int(result[0]), int(result[1]-result[0]))