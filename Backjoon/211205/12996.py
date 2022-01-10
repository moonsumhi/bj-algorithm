# 3 3 1 1
s, a, b, c = map(int, input().split())
d = [[[[-1]*51 for k in range(51)] for j in range(51)] for i in range(51)]

def go(s, a, b, c):

    if s == 0:
        if a == 0 and b == 0 and c == 0:
            return 1
        else:
            return 0

    if a < 0 or b < 0 or c < 0:
        return 0

    if d[s][a][b][c] != -1:
        return d[s][a][b][c]

    ans = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if i+j+k == 0:
                    continue
                ans += go(s-1, a-i, b-j, c-k)
    d[s][a][b][c] = ans

    return d[s][a][b][c]

print(go(s, a, b, c))