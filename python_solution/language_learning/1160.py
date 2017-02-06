i=0
result = []
while 1:
    input_line = input()
    repeat_str = ''
    repeat_len = 0
    if input_line == '.':
        break
    j = 0
    input_len = len(input_line)
    while j < input_len:
        
        if repeat_str == '':
            repeat_str += input_line[j]
            repeat_len += 1
        else:
            if repeat_str[0] == input_line[j]:
                tmp_str = ''
                tmp_len = 0
                pos = 0
                while  j < input_len:
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
    
    if repeat_len == 0:
        result.append(0)
    else:
        result.append(int(input_len/repeat_len))
    i = i+1
    
for x in result:
    print(x)