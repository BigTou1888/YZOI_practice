n = input()
n = int(n)

score = input().split()
i = 0
cnt=[]
while i<101:
    cnt.append(0)
    i=i+1
i=0
maxium=0
while i<n:
    score_u=int(score[i])
    cnt[score_u]=cnt[score_u]+1
    if maxium < cnt[score_u]:
        maxium = cnt[score_u]
    i=i+1
i=0
while i<=100:
    if cnt[i] == maxium:
        print(i, maxium)
    i=i+1