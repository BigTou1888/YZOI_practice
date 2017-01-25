import math

in_char = input().split()
num = 0
param = []
while in_char[0] != "E":
   param.append(in_char)
   in_char = input().split()
   num = num+1

i = 0

while i < num:
    # T: weight 1
    T = 0 
    # D: weight 2
    D = 0
    # H: weight 4
    H = 0
    weight = 0
    for x in range(2):
        if param[i][x*2] == 'T':
            weight = weight+1
            T = float(param[i][x*2+1])
        elif param[i][x*2] == 'D':
            weight = weight+2
            D = float(param[i][x*2+1])
        elif param[i][x*2] == 'H':
            weight = weight+4
            H = float(param[i][x*2+1])
    if weight == 3:
        # calculate H
        e = 6.11 * math.exp(5417.7530 * ((1/273.16) - (1/(D+273.16))))
        h_tmp = (0.5555)* (e - 10.0)
        H = T+h_tmp
    elif weight == 5:
        #calculate D
        h_tmp = H-T
        e = h_tmp/0.5555+10.0
        D = 1/ ( (1/273.16) - math.log(e/6.11)/5417.7530 ) - 273.16
    elif weight == 6:
        #calculate T
        e = 6.11 * math.exp (5417.7530 * ((1/273.16) - (1/(D+273.16))))
        h_tmp = (0.5555)* (e - 10.0)
        T = H-h_tmp
    print ("T %.1f D %.1f H %.1f" % (T, D, H))
    i = i+1