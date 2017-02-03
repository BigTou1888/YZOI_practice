
def gcd (a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif (a%2==0) & (b%2==0):
        return 2 * gcd(a/2, b/2)
    elif (a%2 == 0) & (b%2!=0):
        return gcd(a/2, b)
    elif (a%2!=0) & (b%2==0):
        return gcd(a, b/2)
    elif (a%2!=0) & (b%2!=0):
        if a<b:
            return gcd((b-a), a)
        else:
            return gcd((a-b), b)
        
         
def gcd_n (test_array, n):
    if n ==1:
        return int(test_array[0])
    else:
        head_value = int(test_array.pop(0))
        n=n-1
        return gcd(head_value, gcd_n(test_array, n))
    
    
def gcd_lcm (a, b, c): 
    # b, previous gcd, c, previous lcm
    gcd_value = gcd(a, b)
    lcm_value = a*c/gcd(a, c)
    return [gcd_value, lcm_value]
def gcd_lcm_n(test_array, n):
    head_value = int(test_array[0])
    if n==1:
        return [head_value, head_value]
    else:
        test_array.pop(0)
        n = n-1
        gcd_lcm_arr = gcd_lcm_n(test_array, n)
        return gcd_lcm(head_value, gcd_lcm_arr[0], gcd_lcm_arr[1])
    

        
n = int(input())

    

input_line = input().split()


gcd_lcm_value = gcd_lcm_n(input_line, n)
print(int(gcd_lcm_value[0]))
print(int(gcd_lcm_value[1]))


