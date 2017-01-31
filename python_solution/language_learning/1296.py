n = int(input())
test_value = n

while test_value >=10:
    print(int(test_value), end=' ')
    tmp_value = test_value
    test_value = 1
    while tmp_value >=10:
        test_value = test_value * (tmp_value%10)
        tmp_value = int(tmp_value/10)
    test_value = test_value * tmp_value
print (int(test_value))