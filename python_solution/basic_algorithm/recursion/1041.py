def recur_result (num):
    addon = 2*(num-1)
    if num == 1:
        return 2
    else:
        return recur_result(num-1)+addon

n = int(input())
print(recur_result(n))
