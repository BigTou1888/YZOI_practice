
n = int(input())
tri=[]
i=0

while i<n:
    j=0
    num = i+1
    row = []
    while j<num:
        
        if j == 0: #first
            print_value = 1
        elif j == i: # last
            print_value = 1
        else: #middle
            print_value = tri[i-1][j-1] + tri[i-1][j]
        
        print(print_value, end='')
        j+=1
        if j==num:
            print('')
        else:
            print(' ', end='')
        row.append(print_value)
    tri.append(row)
    i+=1