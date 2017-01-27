c = input()

con = list(c)

i = 0
while i<len(con):
    con[i] =chr( ord(con[i]) -7)
    i = i+1
        
str_con = ''.join(con)
print (str_con)

