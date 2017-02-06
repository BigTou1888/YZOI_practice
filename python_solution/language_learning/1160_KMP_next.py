def getNext(input_string, str_len):
    result = []
    result.append(-1)
    j = 0
    k = -1
    while j < str_len :
        if k == -1:
            k = k+1
            j = j+1
            result.append(k)
        elif input_string[j] == input_string[k]:
            k = k+1
            j = j+1
            result.append(k)
        else:
            k = result[k]
    return result
    




i=0
result = []
while 1:
    input_line = input()
    input_len = len(input_line)
    if input_line == '.':
        break
    next = getNext(input_line, input_len)
    
    repeat_len = input_len- next[input_len]
    if input_len%repeat_len == 0:

        result_tmp = input_len/repeat_len
        result_tmp = int(result_tmp)
        result.append(result_tmp)
    else:
        result.append(1)
    
for x in result:
    print(x)