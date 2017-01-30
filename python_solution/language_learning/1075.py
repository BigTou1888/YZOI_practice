
def SumOfDivisors(num):
    i=1
    test_num = num
    sum=0
    while i < test_num/2+1:
        if num%i == 0:
            sum = sum+i
            if (num/i != i) & (num/i !=num):
                sum = sum+num/i
            if num/i < test_num:
                test_num = num/i
        i = i+1
    return int(sum)
            
index = 1
while index <= 100000:
 #   print ("testing ", index)
    a=index
    a_sum = SumOfDivisors(a)
 #   print("a =", a, "a_sum =", a_sum)
    if (a_sum>a) & (a_sum<=100000):
        b = a_sum
        b_sum = SumOfDivisors(b)
        if b_sum == a:
            print (a, b)
    index = index+1

