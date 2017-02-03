


a=input()

k = 0


cur_value = 1
total_dig_num = 1

pos = 0
upper = 10
string_buf_len = 0
string_buf = ''

while 1:
    while cur_value < upper:
        tmp_value = cur_value
        cur_dig_num = 0
        tmp_upper = upper
        while cur_dig_num < total_dig_num:
            cur_digit = int(tmp_value / (tmp_upper/10))
            tmp_value = tmp_value - int(cur_digit*tmp_upper/10)
            cur_digit = chr(cur_digit+ord('0'))

            if string_buf_len == len(a) :
                string_buf = string_buf[1:]
                string_buf = string_buf + cur_digit
                if string_buf == a:
                    print(pos - len(a) +1 +1)
                    exit(0)
            else:
                string_buf = string_buf + cur_digit
                string_buf_len = string_buf_len+1
                if string_buf_len == len(a):
                    if string_buf == a:
                        print(pos - len(a) +1 +1)
                        exit(0)
            cur_dig_num = cur_dig_num +1
            pos = pos+1
            tmp_upper = int(tmp_upper/10)
        cur_value = cur_value + 1
    upper = upper*10
    total_dig_num = total_dig_num+1
        