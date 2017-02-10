inp = input().split()
n=int(inp[0])
m=int(inp[1])

global star
star = []
i=0
while i<n:
    inp=input()
    j=0
    star.append([])
    while j<m:
        if inp[j] == '#':
            location=[i,j]
            star[i].append(j)
        j+=1
    i+=1
result=0
i=0

def star_graph(x_a, y_a):

    i=0
    find = 0
    if (x_a <0) | (x_a >=n):
        return
    if (y_a <0) | (y_a >=m):
        return
    if len(star[x_a])==0: 
        return
    for x in star[x_a]:
        if x<y_a:
            i+=1
        elif x==y_a:
            find=1
            break
        else:
            break
    if find:
        star[x_a].pop(i)
        star_graph(x_a-2, y_a)
        star_graph(x_a-1, y_a-1)
        star_graph(x_a-1, y_a)
        star_graph(x_a-1, y_a+1)
        star_graph(x_a, y_a-2)
        star_graph(x_a, y_a-1)
        star_graph(x_a, y_a+1)
        star_graph(x_a, y_a+2)
        star_graph(x_a+1, y_a-1)
        star_graph(x_a+1, y_a)
        star_graph(x_a+1, y_a+1)
        star_graph(x_a+2, y_a)
    else:
        return
    
while i <n:

    while len(star[i])!=0:

        star_graph(i, star[i][0])
        result+=1
    i+=1

print(result)
        