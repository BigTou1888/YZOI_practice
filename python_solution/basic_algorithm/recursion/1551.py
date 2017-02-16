global x1, x2, y1, y2
def path_find (b,c ):
    p1=[(c[0]+2), (c[1]+1)]
    p2=[(c[0]+1), (c[1]+2)]
    p3=[(c[0]-1), (c[1]+2)]
    p4=[(c[0]-2), (c[1]+1)]
    p5=[(c[0]-2), (c[1]-1)]
    p6=[(c[0]-1), (c[1]-2)]
    p7=[(c[0]+1), (c[1]-2)]
    p8=[(c[0]+2), (c[1]-1)]
    
    path=[]
    x=0
    while x<=b[0]:
        y=0
        path_row=[]
        while y<=b[1]:
            if (x==0)& (y==0):
                path_row.append(1)
            elif ([x,y] == p1)|([x,y] == p2)|([x,y] == p3)|([x,y] == p4)|([x,y] == p5)|([x,y] == p6)|([x,y] == p7)|([x,y] == p8)|([x,y] == c):
                path_row.append(0)
            elif x==0:
                path_row.append(path_row[y-1])
            elif y==0:
                path_row.append(path[x-1][0])
            else:
              
                path_row.append(path_row[y-1]+path[x-1][y])
            y+=1
        #print(path_row)
        path.append(path_row)
        x+=1
    return path[b[0]][b[1]]
    
cm = input().split()
b=[int(cm[0]),int(cm[1])]
c=[int(cm[2]),int(cm[3])]
print(path_find(b,c))

