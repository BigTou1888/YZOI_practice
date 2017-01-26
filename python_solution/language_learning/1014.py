v = input().split()
y = int(v[0])
m = int(v[1])
if (m == 1) | (m==3) | (m==5) | (m==7) | (m==8)| (m==10)| (m==12) :
   print(31)
elif (m==2):
    if y%4==0:
        if y%400 == 0:
            print(29)
        elif y%100 == 0:
            print(28)
        else:
            print(29)
    else:
        print(28)
else:
    print(30)