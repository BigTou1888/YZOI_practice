
door = []
i = 0
cnt = 100
while i < cnt:
    door.append(0)
    i = i+1
w = 1
while w < (cnt+1):
    d = 0
    while d < cnt:
        if (d+1)%w ==0:
            if door[d] == 0:
                door[d] = 1
            else:
                door[d] = 0
        d = d+1
    w = w+1

            
d = 0
while d < cnt-1:
    if door[d] == 1:
        print (d+1, end=" ")
    d = d+1

if door[99] == 1:
    print (100)

    

