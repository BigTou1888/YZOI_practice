def mine_check_around(mine, row,col,n,m):
    if row <0: 
        return 0
    if row > n-1:
        return 0
    if col < 0:
        return 0
    if col > m-1:
        return 0
    if mine[row][col] == '*':
        return 1
    else:
        return 0
def mine_check(mine, row, col, n, m):

    mine_cnt0 = mine_check_around(mine, row-1,col-1,n,m) + mine_check_around(mine, row-1,col,n,m) +  mine_check_around(mine, row-1,col+1,n,m)
    mine_cnt1 = mine_check_around(mine, row,col-1,n,m) + mine_check_around(mine, row,col,n,m) +  mine_check_around(mine, row,col+1,n,m)
    mine_cnt2 = mine_check_around(mine, row+1,col-1,n,m) + mine_check_around(mine, row+1,col,n,m) +  mine_check_around(mine, row+1,col+1,n,m)
    mine_cnt = mine_cnt0+mine_cnt1+mine_cnt2

    return chr(ord('0')+mine_cnt)


not_first_line = 0
entry = 1
while 1:

    input_line = input().split()
    n = int(input_line[0])
    m = int(input_line[1])
    if (n==0) & (m==0):
        break
    mine=[]
    row=0
    while row<n:
        mine_row=[]
        col=0
        row_str = input()
        mine.append(row_str)
        row+=1
    row=0
    if(not_first_line):
        print('')
    print('Field #%0d:' % entry)
    not_first_line = 1
    while row<n:
        col=0
        while col<m:
            if mine[row][col] == '.':
                ctr=(mine_check(mine, row, col, n, m))
            else:
                ctr='*'
            
            col+=1
            print(ctr,end='')
            if col ==m:
                print('')
        row+=1
    
    entry+=1
        