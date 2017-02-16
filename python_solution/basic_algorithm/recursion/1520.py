n=int(input())

def divisor_2(m):
    div=2
    pow=0
    result=''
    first = 1
    while m!=0:
        if ((m%div)!=0):
            pow_str=''
            if pow==0:
                pow_str='2(0)'
            elif pow==1:
                pow_str='2'
            elif pow == 2:
                pow_str = '2(2)'
            else:
                pow_str = '2('+divisor_2(pow)+')'
                
            m -= (m%div)
            if first:
                result = pow_str
                first=0
            else:
                result = pow_str +'+'+ result
        pow+=1
        div *=2
    return result
print(divisor_2(n))