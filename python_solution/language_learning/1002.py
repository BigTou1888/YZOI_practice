input_line = input()

cnt = {}
i = 0
while i < 10:
    cnt[chr(i+ord('0'))] = 0
    i = i+1
i = 0
while i < 26:
    cnt[chr(i+ord('a'))] = 0
    i = i+1
i=0
while i < 26:
    cnt[chr(i+ord('A'))] = 0
    i = i+1
i = 0
length = len(input_line)
while i <length:

    x = input_line[i]
    if x=='?':
        break
    if (x in cnt) :
        cnt[x] +=1
    i = i+1
    
i = 0
while i < 10:
    x=chr(i+ord('0'))
    if (cnt[x] != 0):
        print(x, cnt[x])
    i = i+1
i = 0
while i < 26:
    x=chr(i+ord('a'))
    x_up = chr(i+ord('A'))
    count = cnt[x]+cnt[x_up]
    if count!=0:
        print(x, count)
    i = i+1
