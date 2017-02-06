tran={}
tran['a'] = '2'
tran['b'] = '2'
tran['c'] = '2'
tran['d'] = '3'
tran['e'] = '3'
tran['f'] = '3'
tran['g'] = '4'
tran['h'] = '4'
tran['i'] = '4'
tran['j'] = '5'
tran['k'] = '5'
tran['l'] = '5'
tran['m'] = '6'
tran['n'] = '6'
tran['o'] = '6'
tran['p'] = '7'
tran['q'] = '7'
tran['r'] = '7'
tran['s'] = '7'
tran['t'] = '8'
tran['u'] = '8'
tran['v'] = '8'
tran['w'] = '9'
tran['x'] = '9'
tran['y'] = '9'
tran['z'] = '9'


n = int(input())
input_arr = []
i = 0
letter2digit=[]
while i < n:
    input_line = input()
    length = len(input_line)
    j = 0
    digit_str = ''
    while j < length:
        digit =  tran[input_line[j]]
        digit_str = digit_str + digit
        j = j+1
    letter2digit.append(digit_str)
    i = i+1
s = input()
len_s = len(s)
result = 0
for x in letter2digit:
    if len(x) != len_s:
        continue
    else:
        j = 0
        while j < len_s:
            if x[j] != s[j]:
                break
            else:
                j += 1
        if j == len_s:
            result += 1

print(result) 