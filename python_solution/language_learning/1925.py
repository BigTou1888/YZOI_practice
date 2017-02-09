input_line = input().split()
n=int(input_line[0])
m=int(input_line[1])

i=0
result=[]
while i<n:
    input_line = input().split()
    pos=1
    for x in input_line:
        if int(x) !=0:
            result.append([i+1, pos, int(x)])
        pos+=1
    i+=1
    
for x in result:
    print(x[0], x[1], x[2])