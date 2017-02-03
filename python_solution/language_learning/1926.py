
def factorial_rcur(value):
    if value ==0 :
        return 1
    elif value == 1:
        return 1
    else:
        return value * factorial_rcur(value-1)

i=5
sum = 0
while i<=11:
    sum = sum+factorial_rcur(i)
    i = i+2
print (sum)
