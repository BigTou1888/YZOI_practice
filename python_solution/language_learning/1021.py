
n = int(input())
num_a = input().split()

minum = int(num_a[0])
length = len(num_a)
i = 0
pos = 0
while i < length:
    cur_value = int(num_a[i])
    if cur_value < minum:
        pos = i
        minum = cur_value
    
    i = i+1

num_a[pos] = num_a[0]
num_a[0] = minum

i=0

print(num_a[0], end='')
i=1
while i<length:
    print('', num_a[i], end='')
    i+=1
print('')
