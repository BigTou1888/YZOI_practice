global n, m
input_line = input().split()
n = int(input_line[0])
m=int(input_line[1])
global pair
pair=[]
def ingre(ingre_num, ingre_vec):
    if ingre_num==n:
        return 1
    else:
        if (ingre_vec & pair[ingre_num]) !=0:
            return ingre(ingre_num+1, ingre_vec)
        else:
            return (ingre(ingre_num+1, (ingre_vec|(1<<ingre_num))) + ingre(ingre_num+1, ingre_vec))
        



i=0
while i < n:
    pair.append(0)
    i+=1
i=0
while i < m:   
    input_line = input().split()
    a = int(input_line[0])
    b = int(input_line[1])
    a-=1
    b-=1
    pair[a] = pair[a] | (1<<b)
    pair[b] = pair[b] | (1<<a)
    i+=1

print(ingre(0,0))