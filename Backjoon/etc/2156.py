N = int(input())
Wines = [0]
for _ in range(N):
    Wines.append(int(input()))
dp = [[0,0] for _ in range(N+1)]

for i in range(1, N+1):

    if i == 1:
        dp[1][0] = 0
        dp[1][1] = Wines[1]
        continue
    dp[i][0] = max(dp[i-1][0], dp[i-1][1])
    dp[i][1] = max(dp[i-2][1]+Wines[i], dp[i-2][0]+Wines[i-1]+Wines[i])
print(max(dp[N][0], dp[N][1]))


# 6
# 6
# 10
# 13
# 9
# 8
# 1