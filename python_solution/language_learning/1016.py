
n = 1
while (n<=999) & ( n>=1):
    if (n%3)==0:
        tmp = n
        while tmp > 0:
            if (tmp%10) ==5:
                print(n)
                break
            else:
                tmp = int(tmp/10)
    n = n+1

