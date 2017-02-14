inp = input().split()
l=int(inp[0])
m=int(inp[1])

tree=[]
total_num = 0
i=0
while i<m:
    inp=input().split()
    start = int(inp[0])
    end = int(inp[1])

    if start < 0: start = 0
    if end > l : end=l
    total_num_old = total_num
    j=0
    while j<total_num_old:
        if end < tree[j][0]:
            tree.insert(j, [start, end])
            total_num+=1
            break
        elif end==tree[j][0]:
            tree[j][0] = start
            break
        elif end <= tree[j][1]:
            if start < tree[j][0]:
                tree[j][0] = start
                break
            else:
                break
        elif end >tree[j][1]:
            if start<=tree[j][0]:               
                tree[j][0]=start
                start = tree[j][1]+1
            elif (start > tree[j][0]) & (start <= tree[j][1]):
                start = tree[j][1]+1
        
        j+=1
    if j==total_num_old:
        tree.append([start, end])
        total_num+=1
    i+=1

total_tree = l + 1   

for x in tree:
    total_tree -=(x[1]-x[0]+1)
print(total_tree)