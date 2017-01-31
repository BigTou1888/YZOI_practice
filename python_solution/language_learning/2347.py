n = int(input())
input_arr = []
i = 0
while i < n:
    input_arr.append(int(input()))
    i=i+1
    

sum = 0
for x in input_arr:
    pow = x%10
    num = int(x/10)
    j =0
    val = 1
    while j < pow:
        val = val*num
        j = j+1
    sum = sum+val
    
print(sum)


