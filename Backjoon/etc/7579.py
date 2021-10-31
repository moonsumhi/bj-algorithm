N, M = map(int, input().split())
bytes = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(sum(costs)+1)] for _ in range(N+1)]
ans = float('inf')
for i in range(1, N+1):
    byte = bytes[i]
    cost = costs[i]
    for j in range(1, sum(costs)+1):
        if cost > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost]+byte)

        if dp[i][j] >= M:
            ans = min(ans, j)

print(ans)
