v = int(input())

if v%4==0:
    if v%400 == 0:
        print("Yes")
    elif v%100 == 0:
        print("No")
    else:
        print("Yes")
else:
    print("No")