
    
t = 1

total = 0

while t < 100:
    f = 1
    tw = 1
    o = 1
    rem_10 = 1000-t*10
    while f < rem_10/5:
        rem_5 = 1000-t*10-f*5
        #2tw+o = rem_5
        #tw+o = 400-f-t
        #tw=rem_5+f+t-400
        #o=800-rem_5-2f-2t      
        if (rem_5 + f+t-400 >0) & (800-rem_5-2*f-2*t>0):
            total = total + 1
        f = f+1
    t = t+1

print(total)
            
        


