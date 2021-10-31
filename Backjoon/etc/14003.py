N = int(input())
arr = list(map(int, input().split()))
dp = [[arr[i]] for i in range(N)]

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            if len(dp[i]) < len(dp[j])+1:
                dp[i] = dp[j] + [arr[i]]

print(len(dp[-1]))
print(dp[-1])

# 6
# 10 20 10 30 20 50