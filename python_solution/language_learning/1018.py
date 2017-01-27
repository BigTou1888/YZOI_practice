
d = int(input())
i = 1
sum = 0
while i <= d:
    n = 1
    sub_sum = 0
    while n<=i:
        sub_sum = sub_sum+n
        n = n+1
    sum = sum+sub_sum
    i = i+1

        

print(sum)

