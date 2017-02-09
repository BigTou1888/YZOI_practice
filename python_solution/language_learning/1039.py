
n = int(input())


i=0
result=[]
while i < n:
    input_line = input().split()
    m=int(input_line[0])
    d=int(input_line[1])
    s = (int(m*2+d))%3
    result.append(s)
    i+=1
i=0
for x in result:
    if x==0:
        print("Boding")
    elif x==1:
        print("Normal")
    else:
        print("Propitious")
