cm=input().split()
a=int(cm[0])
n=int(cm[1])
m=int(cm[2])
x=int(cm[3])

a_cnt=1
y_cnt=0
a_cnt_x=0
y_cnt_x=0
up_a_cnt_2=0
up_y_cnt_2=0
up_a_cnt_1=0
up_y_cnt_1=0
i=0
while i<n:
    up_a_cnt_0=0
    up_y_cnt_0=0
    if i==0:
        up_a_cnt_0 = 1
    elif i == 1:
        up_y_cnt_0 = 1
    elif i==(n-1):
        up_a_cnt_0=0
        up_y_cnt_0=0
    else :
        up_y_cnt_0 = up_y_cnt_2+up_y_cnt_1
        up_a_cnt_0 = up_a_cnt_2+up_a_cnt_1
        a_cnt = a_cnt+up_a_cnt_0-up_a_cnt_1
        y_cnt = y_cnt+up_y_cnt_0-up_y_cnt_1
    
    if i == (x-1):
        a_cnt_x=a_cnt
        y_cnt_x=y_cnt
    
    
    up_a_cnt_2 = up_a_cnt_1
    up_y_cnt_2 = up_y_cnt_1
    up_a_cnt_1 = up_a_cnt_0
    up_y_cnt_1 = up_y_cnt_0
    i+=1

y=0
if y_cnt!=0:
    y = (m - a*a_cnt)/y_cnt

if (m - a*a_cnt)%y_cnt ==0:
    print(int(y*y_cnt_x+a*a_cnt_x))
else:
    print("No answer.")