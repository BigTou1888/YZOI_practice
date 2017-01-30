i = 100

while i < 1000:
    tmp = i
    a = tmp%10
    tmp = int(tmp/10)
    b=tmp%10
    c = int(tmp/10)
    
    if a*a*a+b*b*b+c*c*c == i:
        print(i)
    
    i = i+1
