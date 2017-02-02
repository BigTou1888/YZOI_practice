result=[]

while 1:
    input_line = input().split('+')
    if input_line[0] == '#': break
    else:
        sum=0
        for x in input_line:
            sum = sum+int(x)
            
        result.append(sum)
        
for x in result:
    print(x)