p=[]
k=[]
h=[]
t=[]
p_cnt=0
k_cnt=0
h_cnt=0
t_cnt=0
i=0
while i<13:
    p.append(0)
    k.append(0)
    h.append(0)
    t.append(0)
    i+=1

s = input()

len_s = len(s)
card_cnt = int(len_s/3)
i=0
greska=0
while i< card_cnt:
    c=s[i*3]
    ten=s[i*3+1]
    one=s[i*3+2]
    val = int(ten)*10+int(one)
    if c=='P':
        if p[val-1] ==1:
            greska=1
            break
        else:
            p[val-1] +=1
            p_cnt+=1
    elif c=='K':
        if k[val-1] ==1:
            greska=1
            break
        else:
            k[val-1] +=1
            k_cnt+=1
    elif c=='H':
        if h[val-1] ==1:
            greska=1
            break
        else:
            h[val-1] +=1
            h_cnt+=1
    elif c=='T':
        if t[val-1] ==1:
            greska=1
            break
        else:
            t[val-1] +=1
            t_cnt+=1
    i+=1
if greska:
    print("GRESKA")
else:
    print(13-p_cnt, 13-k_cnt, 13-h_cnt, 13-t_cnt)