input_line = input().split()
m=int(input_line[0])
n=int(input_line[1])

mattrix = []
i=0
while i < m:
    row = input().split()
    mattrix.append(row)
    i+=1
i=0
while i < n:
    j=0
    while j<m:
        print(mattrix[j][i], end='')
        if j < m-1:
            print(' ', end='')
        else:
            print('')
        j+=1
    i+=1
    
    