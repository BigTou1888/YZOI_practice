
def printLine(line_num, entry_num):
    i = 0
    start = 5
    while i < entry_num:
        
        if i == (entry_num-1):
            print ("%3d" % start)
        else:
            print("%3d" % start, end='')
        
        if i < entry_num - line_num-1 :
            start = start - 1

        i = i+1
            
entry = int(input())
i = 0
while i < entry:
    printLine(i, entry)
    i = i+1
