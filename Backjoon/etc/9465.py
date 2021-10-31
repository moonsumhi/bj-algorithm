T = int(input())
for _ in range(T):
    col = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0]*col for _ in range(2)]

    for i in range(col):
        if i == 0:
            dp[0][0], dp[1][0] = stickers[0][0], stickers[1][0]
        elif i == 1:
            dp[0][1], dp[1][1] = dp[1][0] + stickers[0][1], dp[0][0] + stickers[1][1]
        else:
            dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + stickers[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + stickers[1][i]
    print(max(dp[0][col-1], dp[1][col-1]))

# 2
# 5
# 50 10 100 20 40
# 30 50 70 10 60
# 7
# 10 30 10 50 100 20 40
# 20 40 30 50 60 20 80