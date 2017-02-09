input_line = input().split()
n = int(input_line[0])
m = int(input_line[1])
stride_rank= int(n/m)
rank_a = []
score_a = []
i=0
while i < n:
    tmp_rank = i+1
    score = int(input())
    score_a.append(score)
    maxi_low_num = 0
    j=0
    while j < i:
        if score_a[j] <= score:
            if score_a[j] >= maxi_low_num:
                tmp_rank = rank_a[j]
                maxi_low_num = score_a[j]
            if score_a[j]!=score:
                rank_a[j] +=1
        j+=1
        
    rank_a.append(tmp_rank)
    i+=1
    
index = int(input())

print("%d" % ((rank_a[index-1]-1)/stride_rank + 1))


