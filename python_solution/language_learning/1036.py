def long_sub(a, b, did_reorder):
    result = []
    length_a = len(a)
    length_b = len(b)
    
    if did_reorder:
        length = length_a
        i = 0
        c=0
        while i < length:
            a_cur = 0
            b_cur = 0

            a_cur = int(a[length_a-i-1])
            
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
        return result
    else:
        if length_a < length_b:
            result=long_sub(b, a, 1)
            result.insert(0, '-')

        elif length_a > length_b:
            
            result=long_sub(a, b, 1)
        else:
            i =0
            while i < length_a:
                if int(a[i]) > int(b[i]):
                    result = long_sub(a, b, 1)
                    break
                elif int(a[i]) < int(b[i]):
                    result = long_sub(b, a, 1)
                    result.insert(0, '-')
                    break
                else:
                    i=i+1
        return result
            

            
        



a=input()
b=input()

result = long_sub(a, b, 0)

if result[0] == '-':
    print ('-', end='')
    result.pop(0)

starting_0 = 1
for x in result:
    if (x == 0) & starting_0: continue
    else:
        starting_0 = 1
        print(x, end='')
print ('')
