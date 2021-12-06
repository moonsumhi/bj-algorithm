n = int(input())
block = input()
d = [-1]*n
d[0] = 0

def get_prev(i):
    if block[i] == 'J':
        return 'O'
    if block[i] == 'O':
        return 'B'
    if block[i] == 'B':
        return 'J'

for i in range(n):
    now = block[i]
    prev = get_prev(i)
    for k in range(0, i):
        if d[k] == -1:
            continue
        if prev != block[k]:
            continue
        if d[i] == -1 or d[i] > d[k]+(i-k)**2:
            d[i] = d[k]+(i-k)**2

print(d)



# 9
# BOJBOJBOJ