i = 1

while i < 1000:
    div=[]
    div_tmp = 1
    while div_tmp <=i/2:
        if i%div_tmp == 0:
            div.append(div_tmp)


        div_tmp=div_tmp+1
    sum = 0
    for x in div:
        sum = sum+x
    if sum == i:
        print(i)
    i = i+1
