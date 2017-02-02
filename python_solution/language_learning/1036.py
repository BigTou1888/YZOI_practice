a=input()
b=input()

c=0
result = []
length_a = len(a)
length_b = len(b)
length = length_a

if length_a < length_b:
    length = length_b

i = 0
while i < length:
    
    a_cur = 0
    b_cur = 0
    
    if i < length_a:
        a_cur = int(a[length_a-i-1])
    else:
        a_cur = 0
    if i < length_b:
        b_cur = int(b[length_b-i-1])
    else:
        b_cur = 0
    if a_cur<(b_cur+c):

        d = 10+a_cur - b_cur - c
        c = 1
    else:

        d=a_cur-b_cur-c
        c=0
    result.insert(0, d)
    i= i+1

sign = sign ^ c
if sign:
    print('-', end='')
starting_0 = 1
for x in result:
    if (x == 0) & starting_0: continue
    else:
        starting_0 = 1
        print(x, end='')
print ('')
