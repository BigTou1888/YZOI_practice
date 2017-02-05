n=int(input())
i=0
result = []
while i<n:
    input_line = input()
    repeat_str = ''
    repeat_len = 0
    if len(input_line) == 0:
        continue
    j = 0
    while j < len(input_line):
        if repeat_str == '':
            repeat_str += input_line[j]
            repeat_len += 1
        else:
            if repeat_str[0] == input_line[j]:
                tmp_str = ''
                tmp_len = 0
                pos = 0
                while  j < len(input_line):
                    if repeat_str[pos] == input_line[j]:
                        tmp_str += input_line[j]
                        tmp_len +=1
                        pos += 1
                        if (tmp_len % repeat_len) == 0 :
                            pos = 0
                    else:
                        repeat_str += tmp_str
                        repeat_str += input_line[j]
                        repeat_len += tmp_len+1
                        break
                    j = j+1
            else:
                repeat_str += input_line[j]
                repeat_len += 1 
        j = j+1
    
    result.append(repeat_len)
    i = i+1
    
i = 0
while i < (n-1):
    print(result[i], end='\n\n')
    i = i+1
print(result[n-1])