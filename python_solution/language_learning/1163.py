def getNext(input_string, str_len):
    result = []
    result.append(-1)
    j = 0
    k = -1
    while j < str_len :
        if k == -1:
            k = k+1
            j = j+1
            result.append(k)
        elif input_string[j] == input_string[k]:
            k = k+1
            j = j+1
            result.append(k)
        else:
            k = result[k]
    return result


def kmp_match(match_str, sample_str, next):
    m = 0
    s = 0
    result = 0
    m_len = len(match_str)
    s_len = len(sample_str)
    
    while m < m_len:          
        if (match_str[m] == sample_str[s]) | (s==-1):
            s +=1
            m +=1
            if s == s_len:
                result += 1
                s = next[s]
        else:
            s = next[s]
    return result

n = int(input())
i = 0
result = []
while i<n:
    sample_str = input()
    match_str = input()
    next = getNext(sample_str, len(sample_str))
    result.append(kmp_match(match_str, sample_str, next))
    i = i+1

for x in result:
    print(x)
    