while 1:

    
    input_line = input()
    i =0
    sum= 0
    while i<len(input_line):
        while (i<len(input_line)):
            value_char = ord(input_line[i])
            if (ord('a')<= value_char <= ord('z') ) | (ord('A')<= value_char <= ord('Z') ):
                sum = sum+1
                while  (i<len(input_line)):
                    value_char = ord(input_line[i])
                    if (ord('a')<= value_char <= ord('z') ) | (ord('A')<= value_char <= ord('Z') ):
                        i=i+1
                    else:
                        break
            i=i+1
        i=i+1
        
    print(sum)