input_str = input()
command = input().split()
error_indict = 1
length = len(input_str)
i = 0
result = []
if command[0] == 'D':
    while i < length:
        if input_str[i] == command[1]:
            error_indict = 0
            result =  input_str[:i] + input_str[i+1:]
            break
        i += 1
    if error_indict:
        print("ERROR")
    else:
        print(result)
elif command[0] == 'I':
    i = length-1
    while i >= 0:
        if input_str[i] == command[1]:
            error_indict = 0
            result = input_str[:i] + command[2] + input_str[i:]
            break
        i -= 1
    if error_indict:
        print("ERROR")
    else:
        print(result)

elif command[0] == 'R':
    while i < length:
        if input_str[i] == command[1]:
            error_indict = 0
            input_str = input_str[:i]+command[2]+input_str[i+1:]
        i += 1
    if error_indict:
        print("ERROR")
    else:
        print(input_str)