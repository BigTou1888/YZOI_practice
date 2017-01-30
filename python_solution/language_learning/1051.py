N = input()
N = int(N)

charactor = ord('A')

i = 0
while i<N:
    space_cnt = 0
    while space_cnt<(N-i-1):
        print(' ', end='')
        space_cnt=space_cnt+1
    char_cnt=2*i+1
    while char_cnt >0:
        print(chr(charactor), end='')
        char_cnt = char_cnt-1
    print('')
    charactor = charactor+1
    i=i+1
    
