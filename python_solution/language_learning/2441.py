l = int(input())
d = int(input())
x = int(input())

def sum_digits( value):
    sum = 0
    test_value  = value
    while test_value !=0:
        sum = sum+test_value%10
        test_value = int(test_value/10)
    return sum

result = d
i=l
while i <= d:
    result = sum_digits(i)
    if result == x:
        print(i)
        break
    i = i+1
    
i=d
while i >=l:
    result = sum_digits(i)
    if result == x:
        print(i)
        break
    i = i-1