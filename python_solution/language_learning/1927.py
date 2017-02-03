
def com_rcur(n, r):
    if r ==0 :
        return 0
    elif r == 1:
        return n
    else:
        return n/r * com_rcur((n-1), (r-1))

input_line = input().split()
n=int(input_line[0])
r=int(input_line[1])
result = com_rcur(n, r)
print (int(result))