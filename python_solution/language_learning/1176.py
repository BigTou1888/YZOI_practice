
str_start = 0

str_end = 0

cur_pos = 0

lowest_pri = 0
lowest_pri_index = 1

def op_analyze(lowest_pri_target): # 0:)(, 1:(), 2:^, 3:*, 4:+    
    global cur_pos
    global length
    global lowest_pri
    global lowest_pri_index
    global command
    global str_start
    global str_end
    str_start = 0
    str_end = 0
    lowest_pri = 0
    lowest_pri_index = 1
    cur_pos = 0
    while cur_pos < length:
        cur_chr = command[cur_pos]
        if cur_chr == '(':
            open_bracket=1
            tmp_pos = cur_pos
            cur_pos+=1
            while open_bracket !=0:
                if command[cur_pos]==')':
                    open_bracket-=1
                elif command[cur_pos]=='(':
                    open_bracket+=1
                cur_pos +=1

            if lowest_pri <=1:
                lowest_pri =1
                if lowest_pri_index == lowest_pri_target:
                    str_start = tmp_pos
                    str_end = cur_pos				
                lowest_pri_index+=1
			

        else:
            op_priority = 0
            if cur_chr == '^':
                op_priority = 2
            elif cur_chr == '*':
                op_priority = 3
            elif cur_chr == '+':
                op_priority = 4
            else:
                op_priority = -1

            if lowest_pri <op_priority:
                lowest_pri=op_priority
                str_start=0
                lowest_pri_index = 1
                if lowest_pri_index == lowest_pri_target:
                    str_end = cur_pos
                else:
                    str_start = cur_pos+1
                lowest_pri_index+=1
            elif lowest_pri ==op_priority:
                if lowest_pri_index == lowest_pri_target:
                    str_end = cur_pos
                elif lowest_pri_index < lowest_pri_target:
                    str_start = cur_pos+1
                lowest_pri_index+=1
				
            cur_pos+=1
                
    if lowest_pri_index == lowest_pri_target:
        str_end = cur_pos
            
            
            
    




def print_op(para_list, pos, name):
    print('op(%d,' % int(para_list[pos]), end='')
    if pos == 0:
        print('%s' % name, end='')
    else:
        print_op(para_list, (pos-1), name)
    print(')', end='')

command_input = input()
n = int(input())
i=0
name = ''
while command_input[i]!=':':
    name+=command_input[i]
    i+=1
command_input = command_input[i+2:]
length = len(command_input)
op_array = []
i=0
print('Expression %s:' % name)
while i<n:
    op_para = input().split()
    
    para_num = len(op_para)
    print_op(op_para, para_num-1, name)
    print('=', end='')
    j=0
    command = command_input
    length = len(command)
    while j<para_num:
        op_analyze(int(op_para[j]))
        #print ("command is", command)
        #print ("str_start is", str_start)
        #print("str_end is", str_end)
        #print("lowest_pri is", lowest_pri)
        if lowest_pri == 1:
            str_start+=1
            str_end-=1
        #print ("str_start is", str_start)
        #print("str_end is", str_end)
        command = command[str_start:str_end]
        length = len(command)
        
        j+=1
    print(command)
        
    i+=1
i=0
