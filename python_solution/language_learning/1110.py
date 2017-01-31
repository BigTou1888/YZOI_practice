result = []
while 1:
    result_tmp = 0
    input_string = input()
    if input_string == '#':
        break
    i = 0
    check_sum = 0
    while i < len(input_string):
        position = i + 1
        char_value = (0 if input_string[i] == ' ' else (ord(input_string[i]) - ord('A')+1))
        check_sum = check_sum+position*char_value
        i = i+1
    result.append(check_sum)
for x in result:
    print(x)