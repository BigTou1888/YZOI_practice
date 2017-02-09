def clear_cnt(cnt):
    i=0
    while i <9:
        cnt[i]=0
        i+=1
    return cnt

sudoku=[]
i=0
fail = 0
cnt = []
while i < 9:
    cnt.append(0)
    i+=1

i=0
while (i < 9) & (~fail):
    row = input().split()
    sudoku.append(row)
    j=0
    while j<9:
        num=int(row[j])
        if cnt[num-1] ==1:
            fail=1
            break
        else:
            cnt[num-1]+=1
        j+=1

    cnt=clear_cnt(cnt)
    
    i+=1

i=0

while (i < 9) & (~fail):

    j=0
    while j<9:
        num=int(sudoku[j][i])
        if cnt[num-1] ==1:
            fail=1
            break
        else:
            cnt[num-1]+=1
        j+=1
    if fail:
        break
    cnt=clear_cnt(cnt)
    
    i+=1

i=0

while (i < 9) & (~fail):

    j=0
    while j<9:
        row_tmp = int(j/3) + int(i/3)*3
        col_tmp = j%3+(i%3)*3
        num=int(sudoku[row_tmp][col_tmp])
        if cnt[num-1] ==1:
            fail=1
            break
        else:
            cnt[num-1]+=1
        j+=1
    if fail:
        break
    cnt=clear_cnt(cnt)
    
    i+=1
if fail:
    print("No")
else:
    print("Yes")


    
    