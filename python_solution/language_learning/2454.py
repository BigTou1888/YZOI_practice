input_line = input().split()
r = int(input_line[0])
s = int(input_line[1])
k = int(input_line[2])

i =0
fly_array = []
while i < r:
    fly_line = input()
    j=0
    fly_array.append([])
    while j < s:

        if fly_line[j] == '*':
            fly_array[i].append(j)
        j = j+1
    i = i+1
        

max_cnt = 0
max_x = 0
max_y = 0

x=0
y=0

while x <= (r-k+1):
    y = 0
    
    while y <= (s-k+1):
        row = x+1
        fly_cnt = 0
        while row < x+k-1:
            for col in fly_array[row]:
                if (col > y) & (col < y+k-1):
                    fly_cnt = fly_cnt+1
                elif col>= y+k-1:
                    break
            row=row+1
        if fly_cnt > max_cnt:
            max_cnt = fly_cnt
            max_x = x
            max_y = y
        y=y+1
    x = x+1

print (max_cnt)

x=0

while x < r:
    y=0
    while y < s:
        
        if ((y == max_y)|(y == (max_y+k-1))) & ((x == max_x) | (x == (max_x+k-1))):
            print ('+', end='')
        elif ((y > max_y) & (y < (max_y+k-1))) & ((x == max_x) | (x == (max_x+k-1))):
            print('-', end='')
        elif ((y == max_y)|(y == (max_y+k-1))) & ((x>max_x) & (x < (max_x+k-1))):
            print ('|', end='')
        elif ((y > max_y) & (y < (max_y+k-1))) & ((x == max_x) | (x == (max_x+k-1))):
            print('-', end='')
        else:
            if len(fly_array[x]) >0:
                if fly_array[x][0] == y:
                    print('*', end='')
                    fly_array[x].pop(0)
                else:
                    print('.', end='')
            else:
                print('.', end='')
        if len(fly_array[x]) >0:
            if fly_array[x][0] == y:
                 fly_array[x].pop(0)
        y=y+1
    print('')
    x=x+1


                