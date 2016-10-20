x = input().split()
in_data = int(x[0])
out_data = 0
loop_cnt = 4
while loop_cnt>0:
    out_data = out_data * 10
    out_data = out_data + in_data % 10
    in_data = in_data // 10
    loop_cnt = loop_cnt-1
print (out_data)
