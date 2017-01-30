N = input()
N = int(N)


charactor = ord('Z')

i = 1
inc = 1
while i!=0:
    space_cnt=0
    while space_cnt <(2*(N-i)) :
        print('', end=' ')
        space_cnt=space_cnt+1
    print(chr(charactor), end='')
    charactor=charactor-1
    if i ==1:
        print('')
    else:
        space_cnt=0
        while space_cnt <(4*(i-2)+3) :
            print('', end=' ')
            space_cnt=space_cnt+1
        print(chr(charactor))
        charactor=charactor-1
    if i == N:
        inc = 0
        i=i-1
    elif inc==1:
        i = i+1
    elif inc==0:
        i=i-1

    
