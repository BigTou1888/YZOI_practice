value = int(input())
value_low = 0
value_high = 0
sum = 0
if value <1 :
    value_low = value
    value_high = 1
else :
    value_low = 1
    value_high = value
i = value_low
while i <= value_high:
    sum = sum + i
    i = i+1
print(sum) 