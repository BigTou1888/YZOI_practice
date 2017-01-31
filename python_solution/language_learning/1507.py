line_input = input().split()

n = int(line_input[0])
i = int(line_input[1])
j = int(line_input[2])

index =1
while index <= n:
    if index == n :
        print("(%d,%d)" % (i, index))
    else:
        print("(%d,%d)" % (i, index), end='')
    index = index+1
    
index =1
while index <= n:
    if index == n :
        print("(%d,%d)" % (index, j))
    else:
        print("(%d,%d)" % (index, j), end='')
    index = index+1
index = 1
# check line by line
while index <= n:
    row_num = index
    col_num = j-(i-index)
    if (col_num >=1) & (col_num <=n):
        if (row_num ==n) | (col_num == n):
            print("(%d,%d)" % (row_num, col_num))
        else:
            print("(%d,%d)" % (row_num, col_num), end='')
    index = index+1
index = 1
# check column by column
while index <= n:
    col_num = index
    row_num = i+(j-index)
    if (row_num >=1) & (row_num <=n):
        if (row_num ==1) | (col_num == n):
            print("(%d,%d)" % (row_num, col_num))
        else:
            print("(%d,%d)" % (row_num, col_num), end='')
    index = index+1


