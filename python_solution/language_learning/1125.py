def print_line(space_num, star_num):
    space_cnt = 0
    while space_cnt < space_num:
        print(' ', end='')
        space_cnt = space_cnt+1
    star_cnt = 0
    while star_cnt < star_num:
        if star_cnt == (star_num-1):
            print('*')
        else:
            print('*', end='')
        star_cnt = star_cnt+1


def print_tree(max, a, b, c):
    line_cnt = 0
    while line_cnt < c:
        star_num = a + line_cnt * b
        space_cnt = (max - star_num) / 2
        print_line(space_cnt, star_num)
        line_cnt = line_cnt+1

l = int(input())

i = 0
a= []
b = []
c =[]
x=0
y=0
max = 0
while i < l:
    line_input = input().split()
    ai = int(line_input[0])
    bi = int(line_input[1])
    ci = int(line_input[2])
    a.append(ai)
    b.append(bi)
    c.append(ci)
    line_max = ai + bi*(ci-1)
    max = (line_max if line_max>max else max)
    i = i+1
line_input = input().split()
x = int(line_input[0])
y = int(line_input[1])
max = (y if y>max else max)   


i = 0
while i < l:
    print_tree(max, a[i], b[i], c[i])
    i = i+1

print_tree(max, y, 0, x)