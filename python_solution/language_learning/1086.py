
def printLine(line_num, entry_num):
    i = 0
    inc = 1
    start = entry_num - line_num
    while i < entry_num:
        
        if i == (entry_num-1):
            print ("%3d" % start)
        else:
            print("%3d" % start, end='')
        
        if start == entry_num:
            inc = 0
        if inc == 1:
            start = start + 1
        else:
            start = start - 1
        i = i+1
            
entry = int(input())
i = 0
while i < entry:
    printLine(i, entry)
    i = i+1
