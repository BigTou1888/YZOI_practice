i = 2992
def sum_dig(value, pow):
    if value < pow:
        return value
    else:
        return value%pow + sum_dig (int(value/pow), pow)
while i < 10000:
    sum_10 = sum_dig(i, 10)
    sum_12 = sum_dig(i, 12)
    
    if sum_10 == sum_12:
        sum_16 = sum_dig(i, 16)
        if sum_10 == sum_16:
            print(i)
    i = i+1

