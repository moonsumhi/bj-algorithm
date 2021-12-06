# 3 3 1 1

n, a, b, c = map(int, input().split())
d = [[[[-1]*(n+1) for _ in range(n+1)] for __ in range(n+1)] for ___ in range(n+1)]

def go(n, a, b, c):

    if n == 0:
        if a == 0 and b == 0 and c == 0:
            return 1
        else:
            return 0
    if a < 0 or b < 0 or c < 0:
        return 0

    if d[n][a][b][c] != -1:
        return d[n][a][b][c]

    d[n][a][b][c] = go(n-1, a-1, b, c) + go(n-1, a, b-1, c) + go(n-1, a, b, c-1) + \
                    go(n-1, a-1, b-1, c) + go(n-1, a-1, b, c-1) + go(n-1, a, b-1, c-1) + go(n-1, a-1, b-1, c-1)

    return d[n][a][b][c]


print(go(n, a, b, c))
