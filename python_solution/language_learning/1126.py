import math
def is_prime (val):
    if val == 1:
        return False
    div_value = 1
    test_value = int(math.sqrt(val))+1
    while div_value < test_value:
        div_value = div_value+1
        if val%div_value == 0:
            break
    if div_value == test_value:
        return True
    else:
        return False
    
result = []
while 1:
    line_input = input().split()
    a = int(line_input[0])
    d = int(line_input[1])
    n = int(line_input[2])
    if (a==0) & (d==0) & (n==0):
        break
    prime_cnt  = 0
    prime_test = a
    i = 0
    while prime_cnt  < n:
        prime_test = a + d*i
        if is_prime(prime_test):
            prime_cnt = prime_cnt+1
        i = i+1
    result.append(prime_test)
    
for x in result:
    print(x)