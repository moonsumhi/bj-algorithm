# 10
# (?([?)]?}?

n = int(input())
s = input()
d = [[-1]*200 for _ in range(200)]

def go(x, y):
    if x == y:
        return 0
    if d[x][y] != -1:
        return d[x][y]
    if x == '?' or y == '?':


    d[x][y] = go(x, y-1) + go(x+1, y)
