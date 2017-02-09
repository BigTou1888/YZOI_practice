input_line = input().split()
n = int(input_line[0])
c = int(input_line[1])

num_v=[]
num = input().split()
length=0
for x in num:
    num_v.append(int(x))
    length+=1
    
max_c = 0
max_step = 0
pos=0
while pos<length:
    total = 0
    total_step = 0
    cur_pos = pos
    while (total < c) & (cur_pos<length):
        while(cur_pos<length):
            if  (total+num_v[cur_pos]) <= c:
                break
            cur_pos +=1
        if cur_pos != length:          
            total+=num_v[cur_pos]
            total_step+=1
            cur_pos+=1
    if total_step>max_step:
        max_step = total_step
    pos+=1
    
print(max_step)