n = int(input())
s = input()
d = [-1]*n
d[0] = 0

def get_next(x):
    if s[x] == 'B':
        return 'O'
    elif s[x] == 'O':
        return 'J'
    else:
        return 'B'


for i in range(n):
    now = s[i]
    nxt = get_next(i)
    for j in range(i, n):
        if d[i] == -1:
            continue
        if s[j] != nxt:
            continue
        cost = (j-i)**2
        if d[j] == -1 or d[j] > d[i] + cost:
            d[j] = d[i] + cost

print(d[n-1])



# 9
# BOJBOJBOJ