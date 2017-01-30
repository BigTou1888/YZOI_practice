N = input()
N = int(N)


charactor = '#'

i = 1
inc = 1
while i!=0:
    space_cnt=0
    pond_cnt =0
    while space_cnt <(N-i) :
        print('', end=' ')
        space_cnt=space_cnt+1
    
    while pond_cnt <i :
        if pond_cnt ==(i-1):
            print(charactor)
        else:
            print(charactor, end=' ')
        pond_cnt = pond_cnt+1
    if i == N:
        inc = 0
        i=i-1
    elif inc==1:
        i = i+1
    elif inc==0:
        i=i-1

    
