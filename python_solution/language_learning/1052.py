def contains7(value):
    if value % 7 == 0:
        return True
    else:
        while value !=0:
            if value % 10 ==7:
                return True
            else:
                value = int(value/10)

n = int(input())
i = 1
while i <= n :
    if contains7(i):
        print (i)
    i = i+1