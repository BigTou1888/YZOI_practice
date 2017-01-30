N = input()
N = int(N)

i = 0
line_x_start = 1
while i<N:
    line_i=0
    line_x_start = line_x_start+i
    line = line_x_start
    while line_i<(N-i):
        if line_i==N-i-1:
            print(line)
        else:
            print(line, end=' ')
        
        line = line+line_i+i+2
        line_i=line_i+1
    i=i+1
    
