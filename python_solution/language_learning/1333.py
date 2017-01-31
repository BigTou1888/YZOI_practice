line_char = []
line_char.append(input())
line_char.append(input())
line_char.append(input())
line_char.append(input())

max = 0
i = 0
char_sta = []
while i < 26:
    char_sta.append(0)
    i = i+1

i = 0
while i < len(line_char):
    j = 0
    while j < len(line_char[i]):
        charactor = line_char[i][j]
        value = ord(charactor) - ord('A')
        if (value >=0) & (value <26):
            char_sta[value] = char_sta[value] +1
            if char_sta[value] > max:
                max = char_sta[value]
        j = j+1
    i = i+1

i = max
while i > 0:
    j =0
    last = 0
    while j < 26:
        if char_sta[j] >= i:
            last = j
        j = j+1
    j = 0
    while  j <= last:
        if char_sta[j] >= i:
            if j != last:
                print ('*', end=' ')
            else:
                print('*')
        else:
            print(' ', end=' ')

        j = j+1
    i = i-1
i = 0
while i < 25:
    print (chr(i + ord('A')), end = ' ')
    i = i+1

print('Z')