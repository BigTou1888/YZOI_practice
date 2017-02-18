import math
def palindrome_len(dig_num, index):

    
    
    h_len = int(dig_num/2)+ (dig_num%2)

    power=math.pow(10,(h_len-1))
    index-=1
    
    result=str(int(power+index))
    result_rev = result[::-1]
    if dig_num%2 == 1:
        result_rev = result_rev[1:]
    result = result+result_rev
    return result

def palindrome(n):
    total=0
    i=0
    total_last=0
    stride=0
    while total <n:
        total_last+=stride
        if i<2:
            stride=9
        elif i>=2:
            if i%2==0:
                stride *=10
        total+=stride
        i+=1
    dig_num=i
    index=n-total_last
    #print("dig_num:", dig_num, "index:", index)
    return palindrome_len(dig_num, index)

while 1:
    n=int(input())
    if n==0:
        break
    else:
        result = palindrome(n)
        print(result)
        
