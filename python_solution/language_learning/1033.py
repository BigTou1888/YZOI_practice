input_line = input().split()
print(len(input_line))

input_line = input()
i =0
sum= 0
while i<len(input_line):
    while (i<len(input_line)):
        if (input_line[i] !=' '):
            sum = sum+1
            while  (i<len(input_line)):
                if (input_line[i] !=' '):
                    i=i+1
                else:
                    break
        i=i+1
    i=i+1
    
print(sum)