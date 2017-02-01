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
    if n =1:
        return int(test_array[0])
    else:
        head_value = int(test_array.pop(0))
        n=n-1
        return gcd(head_value, gcd_n(test_array, n))
    
n = int(input())

input_line = input().split()


