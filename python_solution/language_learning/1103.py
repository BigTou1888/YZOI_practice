result = []
while 1:
    result_tmp = 0
    input_value = input().split()
    arg_list = []
    i = 0
    for x in input_value:
        arg_list.append(int(x)) 
    if arg_list[0] == -1:
        break
    i = 0
    while i < len(arg_list)-1:
        j = 0
        j = i+1
        while j < len(arg_list)-1:
            if ((arg_list[i]/ arg_list[j] == 2) & (arg_list[i] % arg_list[j] ==0)) | ((arg_list[j]/ arg_list[i] == 2) & (arg_list[j] % arg_list[i] ==0)) :
                result_tmp = result_tmp+1
            j = j+1
        i = i+1
    result.append(result_tmp)
for x in result:
    print(x)