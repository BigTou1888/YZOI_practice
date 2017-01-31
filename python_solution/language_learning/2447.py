input_line = input().split()
N = int(input_line[0])
B = input_line[1]


n=4*N
i = 0
domi_suit = [11, 4, 3, 20, 10, 14, 0, 0]
nondomi_suit = [11, 4, 3, 2, 10, 0, 0, 0]
def sym2num (symbol):
    if symbol == 'A':
        return 0
    elif symbol == 'K':
        return 1
    elif symbol == 'Q':
        return 2
    elif symbol == 'J':
        return 3
    elif symbol == 'T':
        return 4
    elif symbol == '9':
        return 5
    elif symbol == '8':
        return 6
    elif symbol == '7':
        return 7
sum = 0
while i< n:
    card = input()
    if card[1] == B:
        sum = sum + domi_suit[sym2num(card[0])]
    else:
        sum = sum + nondomi_suit[sym2num(card[0])]
    i = i+1
    
print(sum)

