param = input().split()
value1 = int(param[0])
value2 = int(param[1])
oper = param[2]
if oper == '+':
    print(value1+value2)
elif oper == '-':
    print(value1-value2)
elif oper == '*':
    print(value1*value2)
elif oper == '/':
    if value2 == 0:
        print("Divided by zero!")
    else :
        print(int(value1/value2))
else:
    print("Invalid operator!")