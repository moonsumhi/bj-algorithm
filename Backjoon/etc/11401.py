N, K = map(int, input().split())

dp = [0] * (N+1)
dp[1] = 1
for i in range(2, N+1):
    dp[i] = (dp[i-1]*i)%1000000007

print(int(dp[N]/(dp[N-K] * dp[K]))%1000000007)

# 5 2