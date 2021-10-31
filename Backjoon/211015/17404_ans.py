INF = int('inf')

n = int(input())
cost = [[0] * n for _ in range(n+1)]
dp = [[0] * n for _ in range(n+1)]

for i in range(1, n+1):
    cost[i][0], cost[i][1], cost[i][2] = map(int, input().split())

answer = INF
for first in range(3):
    for i in range(3):
        if i == first:
            dp[1][i] = cost[1][i]
        else:
            dp[1][i] = INF

    for i in range(2, n+1):
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = cost[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    for i in range(3):
        if i == first:
            continue
        answer = min(answer, dp[n][i])
print(answer)