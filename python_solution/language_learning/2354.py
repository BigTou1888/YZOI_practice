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
    if command[0] == 'UPIT':
        target = int(command[1])

        while total < target:
            cnt[cur_letter] +=1
            if inc:
                if cur_letter == 25:
                    cur_letter = 0
                else:
                    cur_letter +=1
            else:
                if cur_letter == 0:
                    cur_letter = 25
                else:
                    cur_letter -=1

            
            total +=1

        index = ord(command[2]) - ord('a')
        print(cnt[index])
    elif command[0] == 'SMJER':
        target = int(command[1])
        while total < target:
            cnt[cur_letter] +=1
            if inc:
                if cur_letter == 25:
                    cur_letter = 0
                else:
                    cur_letter +=1
            else:
                if cur_letter == 0:
                    cur_letter = 25
                else:
                    cur_letter -=1

            total +=1
        if inc:
            inc = 0
            if cur_letter == 0:
                cur_letter = 24
            elif cur_letter == 1:
                cur_letter = 25
            else:
                cur_letter -=2
        else:
            inc = 1
            if cur_letter == 24:
                cur_letter = 0
            elif cur_letter == 25:
                cur_letter = 1
            else:
                cur_letter +=2

    
    i = i+1