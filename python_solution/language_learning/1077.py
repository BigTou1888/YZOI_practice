
def printLine(line_num, entry_num):
    start = (entry_num-line_num-1)*entry_num+1
    end = (entry_num-line_num) *entry_num
    while start<=end:
        if start == end:
            print("%3d" % start)
        else:
            print("%3d" % start, end='')
        start=start+1
            
entry = int(input())
i = 0
while i < entry:
    printLine(i, entry)
    i = i+1
