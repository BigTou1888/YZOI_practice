waiting_left = True
while 1:
    input_line = input()
    i = 0
    while i < len(input_line):
        if input_line[i] == '\"':
            if waiting_left:
                print('``', end='')
                waiting_left = False
            else:
                print('\'\'', end='')
                waiting_left = True
        else:
            print(input_line[i], end='')
        i = i+1
    print('')