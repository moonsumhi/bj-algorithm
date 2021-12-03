import sys
n = int(sys.stdin.readline())

matrix = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    matrix.append((a,b))

d = [[-1]*n for _ in range(n)]

def go(x, y):
    if d[x][y] != -1:
        return d[x][y]
    if x == y:
        return 0
    if x+1 == y:
        return matrix[x][0]*matrix[x][1]*matrix[y][1]
    for k in range(x,y):
        left = go(x, k)
        right = go(k+1, y)
        if d[x][y] == -1 or d[x][y] > left+right+matrix[x][0]*matrix[k][1]*matrix[y][1]:
            d[x][y] = left+right+matrix[x][0]*matrix[k][1]*matrix[y][1]
    return d[x][y]

print(go(0, n-1))