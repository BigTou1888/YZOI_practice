
N = input()
N = int(N)




i = 1
inc = 1
while i<=N:
    num_print = 1

    space_cnt=0
    pond_cnt =0
    inc = 1
    while space_cnt <(N-i) :
        print('', end='  ')
        space_cnt=space_cnt+1
    
    while num_print > 0:
        
        if (num_print == 1) & (inc == 0):
            print (num_print)
        elif (num_print == 1) & (i==1):
            print (num_print)
        else:
            print(num_print, end=' ')
        
        if num_print == i:
            inc = 0
            num_print = num_print-1
        elif inc == 1:
            num_print = num_print+1
        elif inc == 0:
            num_print = num_print-1
            
    i=i+1

    
