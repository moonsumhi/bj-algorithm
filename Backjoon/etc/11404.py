N = int(input())
M = int(input())
dp = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    dp[a][b] = min(dp[a][b], c)

for i in range(N+1):
    dp[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if dp[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(dp[i][j], end=' ')
    print()



# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4