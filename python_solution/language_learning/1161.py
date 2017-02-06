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
    n = int(input())
    if n ==0:
        break
    input_line = input()
    input_len = len(input_line)

    next = getNext(input_line, input_len)
    
    if i != 0:
        print('')
    print("Test case #%d" % (i+1))

    j = 2
    while j <= n:
        repeat_len = j -next[j]
        if (j %repeat_len == 0) & ((int(j/repeat_len))!=1):
            print (j, int(j/repeat_len))
        j = j+1
    i = i+1