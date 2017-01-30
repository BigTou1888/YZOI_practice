
def printLine(line_num, entry_num):
    i = 0
    while i < entry_num:
        end_string = ''
        if i == (entry_num-1):
            end_string = '\n'
        else:
            end_string = ''
        print_string = '0'
        if(i == (entry_num-line_num-1)):
            print_string = '%3d' % 1
        else:
            print_string = '%3d' % 0
        print (print_string, end=end_string) 
        i = i+1
            
entry = int(input())
i = 0
while i < entry:
    printLine(i, entry)
    i = i+1
