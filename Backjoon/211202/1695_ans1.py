n = int(input())
a = list(map(int, input().split()))
b = a[::-1]
a = [0]+a
b = [0]+b
d = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if a[i] == b[j]:
            d[i][j] = d[i-1][j-1]+1
        else:
            d[i][j] = max(d[i-1][j], d[i][j-1])

print(n-d[n][n])