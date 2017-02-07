def update_cnt(cnt, cur_letter, stride, direction):
    if stride < 26:
        j = 0
        while j < stride:
            cnt[cur_letter] +=1
            if inc :
                if cur_letter == 25:
                    cur_letter = 0
                else:
                    cur_letter +=1
            else:
                if cur_letter == 0:
                    cur_letter = 25
                else:
                    cur_letter -=1
                
            j +=1
    else:
        j = 0
        low = int(stride/26)
        high_num = stride %26
        high = low
        if high_num != 0:
            high += 1
        while j < high_num:
            cnt[cur_letter] += high
            if inc :
                if cur_letter == 25:
                    cur_letter = 0
                else:
                    cur_letter +=1
            else:
                if cur_letter == 0:
                    cur_letter = 25
                else:
                    cur_letter -=1
                
            
            j+=1
        while j < 26:
            cnt[cur_letter] += low
            if inc :
                if cur_letter == 25:
                    cur_letter = 0
                else:
                    cur_letter +=1
            else:
                if cur_letter == 0:
                    cur_letter = 25
                else:
                    cur_letter -=1           
            j+=1     
    return cnt      
n = int(input())
i = 0
inc = 1
total = 0 #total letter
cur_letter = 0 # within 0-25

cnt = []
while i<26:
    cnt.append(0)
    i += 1

i = 0
while i < n:
    command = input().split()
    
    target = int(command[1])
    stride = target - total
    cnt = update_cnt(cnt,  cur_letter, stride, inc)
    total = target
    if inc:
        cur_letter += stride
        cur_letter = cur_letter%26;
    else:
        cur_letter = 26+cur_letter - (stride%26)
        cur_letter = cur_letter%26
    
    if command[0] == 'UPIT':
        index = ord(command[2]) - ord('a')
        print(cnt[index])
    elif command[0] == 'SMJER':
        if inc:
            inc = 0
            cur_letter  = 26+cur_letter-2
            cur_letter = cur_letter%26
        else:
            inc = 1
            cur_letter += 2
            cur_letter = cur_letter%26
        

    i = i+1