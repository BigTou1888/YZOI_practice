
x = int( input())

i = 0
n = []
m = []
while i < x:
    para = input().split()
    n.append(int(para[0]))
    m.append(int(para[1]))
    i = i+1
    
i = 0
while i<x:
    m_tmp = m[i]
    n_tmp = n[i]

    # greatest common divisor, Euclid
    while n_tmp != 0:
        tmp = n_tmp
        n_tmp = m_tmp % n_tmp
        m_tmp = tmp
    gcd = m_tmp
    

    safe_cnt = 0 
    if gcd == 1:
        print(-1)
    else:
        cave = n[i]-1
        while cave >=0:
            if cave % gcd != 0:
                safe_cnt = safe_cnt+1
                if safe_cnt <= 10:
                    print(cave, end = ' ')
                else: 
                    break
            cave = cave -1
        print ("Total=%d" % (n[i] - (n[i]-1)/gcd))
    i = i+1
