a=input().split()
height = int(input())+30
result = 0
for x in a:
    if height>=int(x):
        result+=1
print(result)