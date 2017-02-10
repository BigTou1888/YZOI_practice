def op_analyze(command, cur_pri, start): # 0:)(, 1:(), 2:*, 3:^, 4:+
    if cur_pri == 0:
        while start < len(command):
            
    




def print_op(para_list, pos, name):
    print('op(%d,' % int(para_list[pos]), end='')
    if pos == 0:
        print('%s' % name, end='')
    else:
        print_op(para_list, (pos-1), name)
    print(')', end='')
command = input()
n = int(input())
i=0
name = ''
while command[i]!=':':
    name+=command[i]
    i+=1
command = command[i+2:]
while i<n:
    op_para = input().split()
    print('Expression %s:' % name)
    para_num = len(op_para)
    print_op(op_para, para_num-1, name)
    print('=', end='')
    print('')
    
        
    i+=1