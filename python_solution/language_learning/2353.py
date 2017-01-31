n = int(input())
m = int(input())

m_out = 0
n_out = 0
m_yoda=1
n_yoda=1
m_pow = 1
n_pow = 1
while (m!=0)&(n!=0):
    dig_m = m%10
    dig_n = n%10
    if dig_m > dig_n:
        m_out=m_out + dig_m * m_pow
        m_pow = m_pow *10
        m_yoda = 0
    elif dig_n > dig_m:
        n_out = n_out + dig_n*n_pow
        n_pow = n_pow* 10
        n_yoda = 0
    else:
        m_out = m_out + dig_m * m_pow
        n_out = n_out + dig_n*n_pow
        m_pow = m_pow*10
        n_pow = n_pow*10
        m_yoda = 0
        n_yoda= 0
    m = int(m/10)
    n = int(n/10)
if m !=0:
    m_yoda = 0
    m_out = m_out + m*m_pow
if n!=0:
    n_yoda = 0
    n_out = n_out +n*n_pow
print(('YODA' if n_yoda else n_out))
print(('YODA' if m_yoda else m_out))
    