
def space_print (cnt):
    j = 0
    while j< cnt:
        print (' ', end='')
        j = j+1
    
input_array = input()

space_cnt=0
i = 0    
while i < len(input_array):
    if input_array[i] == '{':
        space_print(space_cnt)
        print ('{')
        i = i+1
        space_cnt = space_cnt+2
    elif input_array[i] == '}':
        space_cnt = space_cnt-2
        space_print(space_cnt)
        if i == (len(input_array)-1):
            print ('}')
            i = i+1
        elif input_array[i+1] == ',':
            print ('},')
            i = i+2
        else:
            print ('}')
            i = i+1
    else:
        space_print(space_cnt)
        while  (input_array[i]!=',') & (input_array[i] !='}'):
            print(input_array[i], end='')
            i = i+1
        if  input_array[i]==',':
            print(',')
            i = i+1
        else:
            print('')    